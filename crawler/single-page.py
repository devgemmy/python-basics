from playwright.sync_api import sync_playwright
from readability import Document
from bs4 import BeautifulSoup

def extract_text_from_html(html: str):
    doc = Document(html)
    # Readability's cleaned HTML
    cleaned_html = doc.summary(html_partial=True)
    title = doc.short_title()
    # Convert cleaned HTML to plain text
    soup = BeautifulSoup(cleaned_html, "html.parser")
    text = "\n".join(line.strip() for line in soup.get_text("\n").splitlines() if line.strip())
    return title, text

url = "https://nugiframes.com/"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(user_agent="text-extractor/1.0 (+contact)")
    page.goto(url, wait_until="networkidle", timeout=60_000)

    # Optional: handle infinite scroll (uncomment if needed)
    # prev_height = 0
    # while True:
    #     page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    #     page.wait_for_timeout(800)
    #     height = page.evaluate("document.body.scrollHeight")
    #     if height == prev_height:
    #         break
    #     prev_height = height

    html = page.content()
    title, text = extract_text_from_html(html)
    print(title)
    print("="*80)
    print(text[:3000])  # write to file instead for real use
    browser.close()
