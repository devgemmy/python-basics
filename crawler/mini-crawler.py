import time, json, urllib.parse as up, tldextract
from collections import deque
from urllib import robotparser
from playwright.sync_api import sync_playwright
from readability import Document
from bs4 import BeautifulSoup

START_URL = "https://nugiinnovations.com/"
PARALLEL_PAGES = 2           # keep small to be polite
DELAY_SECONDS = 0.7          # rate limit
MAX_PAGES = 100              # safety cap

def same_site(url, root):
    a, b = tldextract.extract(url), tldextract.extract(root)
    return (a.domain, a.suffix) == (b.domain, b.suffix)

def absolute(url, base): return up.urljoin(base, url).split("#")[0]

def clean_text_from_html(html):
    doc = Document(html)
    cleaned_html = doc.summary(html_partial=True)
    title = doc.short_title()
    soup = BeautifulSoup(cleaned_html, "html.parser")
    text = "\n".join(l.strip() for l in soup.get_text("\n").splitlines() if l.strip())
    return title, text

# robots.txt
root = f"{up.urlparse(START_URL).scheme}://{up.urlparse(START_URL).netloc}"
rp = robotparser.RobotFileParser()
rp.set_url(up.urljoin(root, "/robots.txt"))
try:
    rp.read()
except Exception:
    pass  # if robots missing, proceed carefully

seen, q = set([START_URL]), deque([START_URL])
results_path = "corpus.jsonl"

with sync_playwright() as p, open(results_path, "w", encoding="utf-8") as out:
    browser = p.chromium.launch(headless=True)
    ctx = browser.new_context(user_agent="text-extractor/1.0 (+contact)")
    pages = [ctx.new_page() for _ in range(PARALLEL_PAGES)]

    def visit(page, url):
        if rp and hasattr(rp, "can_fetch") and not rp.can_fetch("*", url):
            return None, None, []
        try:
            page.goto(url, wait_until="networkidle", timeout=60_000)

            # Optional: auto-scroll if content loads on scroll
            # page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            # page.wait_for_timeout(800)

            html = page.content()
            title, text = clean_text_from_html(html)

            # discover links (after JS render)
            anchors = page.eval_on_selector_all("a[href]", "els => els.map(a => a.getAttribute('href'))")
            links = []
            for href in anchors:
                if not href: continue
                nxt = absolute(href, url)
                if same_site(nxt, START_URL):
                    links.append(nxt)
            return title, text, links
        except Exception:
            return None, None, []

    processed = 0
    while q and processed < MAX_PAGES:
        batch = [q.popleft() for _ in range(min(len(q) + 1, PARALLEL_PAGES))]  # include current
        for page, url in zip(pages, batch):
            title, text, links = visit(page, url)
            if text:
                out.write(json.dumps({"url": url, "title": title, "text": text}, ensure_ascii=False) + "\n")
                processed += 1
            for ln in links:
                if ln not in seen:
                    seen.add(ln)
                    q.append(ln)
            time.sleep(DELAY_SECONDS)

    browser.close()

print(f"Saved cleaned text to {results_path}")
