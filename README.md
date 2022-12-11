# Python-Web-Scraper

This script scrapes articles (using [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)) from 'nature.com' and saves every news article on the page to a separate .txt file on your computer. In its current stage, it only works for https://www.nature.com and its subpages. It is not yet possible to scrape other websites.

## Requirements

-   Python 3
-   Requirements from `requirements.txt`

## Installation

1. Clone the repository

```bash
git clone https://github.com/dan-koller/Python-Web-Scraper
```

2. Create a virtual environment\*

```bash
python -m venv venv
```

3. Install the requirements\*

```bash
pip install -r requirements.txt
```

4. Run the script\*

```bash
python scraper.py
```

_\*) If you are using a virtual environment, you might need to replace `pip` with `pip3` and `python` with `python3`._

## Usage

-   Run the script with `python scraper.py`
-   Enter the amount of pages you want to scrape
-   Enter the topic you want to scrape (e.g. 'News', 'Nature Briefing', etc.)
-   Wait for the script to finish
-   The scraped articles will be saved in the `Page_N` folder(s)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
