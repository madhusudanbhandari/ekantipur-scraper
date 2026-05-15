# Ekantipur Scraper

A Python-based web scraper that extracts structured data from [ekantipur.com](https://ekantipur.com) using Playwright browser automation.

## What It Scrapes

- **Entertainment News** — Top 5 articles from the मनोरञ्जन section including title, image URL, category, and author
- **Cartoon of the Day** — Title, image URL, and cartoonist name from the cartoon section

## Tech Stack

- Python 3.11+
- Playwright (browser automation)
- uv (package manager)

## Installation

### 1. Install uv
**Windows:**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Mac/Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Clone the Repository
```bash
git clone https://github.com/yourusername/ekantipur-scraper.git
cd ekantipur-scraper
```

### 3. Install Dependencies
```bash
uv add playwright
uv run playwright install chromium
```

## Usage

```bash
uv run python scraper.py
```

The script will:
1. Open a Chrome browser automatically
2. Navigate to the entertainment section and extract top 5 articles
3. Navigate to the cartoon section and extract the cartoon of the day
4. Save all extracted data to `output.json`

## Output Format

```json
{
  "entertainment_news": [
    {
      "title": "Article headline here",
      "image_url": "https://...",
      "category": "मनोरञ्जन",
      "author": "Author Name"
    }
  ],
  "cartoon_of_the_day": {
    "title": "Cartoon title",
    "image_url": "https://...",
    "author": null
  }
}
```

