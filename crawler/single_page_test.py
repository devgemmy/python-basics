from playwright.sync_api import sync_playwright
from readability import Document
from bs4 import BeautifulSoup

URL = "https://nugiframes.com/contact.html"

def extract_text_from_html(html: str):
    doc = Document(html)
    cleaned_html = doc.summary(html_partial=True)
    title = doc.short_title()
    soup = BeautifulSoup(cleaned_html, "html.parser")
    text = "\n".join(line.strip() for line in soup.get_text("\n").splitlines() if line.strip())
    return title, text

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)  # if this fails, try channel="chrome"
    page = browser.new_page(user_agent="text-extractor/1.0 (+contact)")
    page.goto(URL, wait_until="networkidle", timeout=60_000)
    html = page.content()
    browser.close()

title, text = extract_text_from_html(html)
print(title)
print("="*80)
print(text[:2000])
