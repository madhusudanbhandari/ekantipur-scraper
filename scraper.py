import json
from playwright.sync_api import sync_playwright

def scrape_ekantipur():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

       
        entertainment_news = scrape_entertainment(page)

        
        cartoon = scrape_cartoon(page)

        browser.close()

        output = {
            "entertainment_news": entertainment_news,
            "cartoon_of_the_day": cartoon
        }

        
        with open("output.json", "w", encoding="utf-8") as f:
            json.dump(output, f, ensure_ascii=False, indent=2)

        print("\nDone! Saved to output.json")
        print(json.dumps(output, ensure_ascii=False, indent=2))


def scrape_entertainment(page):
    print("Going to entertainment section...")
    page.goto("https://ekantipur.com/entertainment")
    page.wait_for_load_state("networkidle")

   
    page.evaluate("window.scrollTo(0, 1000)")
    page.wait_for_timeout(2000)

    articles = []
    cards = page.query_selector_all("div.category")

    for card in cards:
        title_el = card.query_selector("h2 a")
        title = title_el.text_content().strip() if title_el else None

        
        img_el = card.query_selector("figure img")
        image_url = None
        if img_el:
            image_url = img_el.get_attribute("src")
            if not image_url or image_url == "":
                image_url = img_el.get_attribute("data-src")

        
        author_el = card.query_selector("div.author-name a")
        author = author_el.text_content().strip() if author_el else None

        category = "मनोरञ्जन"

        
        if title:
            articles.append({
                "title": title,
                "image_url": image_url,
                "category": category,
                "author": author
            })

        if len(articles) == 5:
            break

    print(f"Found {len(articles)} entertainment articles")
    return articles


def scrape_cartoon(page):
    print("Going to cartoon section...")
    page.goto("https://ekantipur.com/cartoon")
    page.wait_for_load_state("networkidle")
    page.wait_for_timeout(2000)

    try:
        cartoon_wrapper = page.query_selector("div.cartoon-wrapper")

        img_el = cartoon_wrapper.query_selector("img.loaded")
        image_url = img_el.get_attribute("src") if img_el else None

        desc_el = cartoon_wrapper.query_selector("div.cartoon-description p")
        desc_text = desc_el.text_content().strip() if desc_el else ""

        if " - " in desc_text:
            parts = desc_text.split(" - ", 1)
            title = parts[0].strip().rstrip("-").strip()
            author = parts[1].strip() if parts[1].strip() else None
        else:
            title = desc_text
            author = None

        if not title and img_el:
            title = img_el.get_attribute("alt")

        print(f"Cartoon found: {title}")
        return {
            "title": title,
            "image_url": image_url,
            "author": author
        }

    except Exception as e:
        print(f"Cartoon error: {e}")
        return {
            "title": None,
            "image_url": None,
            "author": None
        }



scrape_ekantipur()