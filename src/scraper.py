import os
import requests
from bs4 import BeautifulSoup
from string import punctuation


def main():
    # Define the domain variables
    url = "https://www.nature.com"
    resource = "/nature/articles"
    n_pages, article_type = int(input()), str(input())

    # Define the translation table
    translated = str.maketrans(" ", "_", punctuation)

    # Loop through the pages
    for n in range(1, n_pages + 1):
        os.makedirs(f"Page_{n}", exist_ok=True)
        r = requests.get(f"{url}{resource}", params={"year": "2020", "page": n})
        soup = BeautifulSoup(r.content, "html.parser")

        # Find the articles
        articles = [
            article
            for article in soup.find_all("article")
            if article.find("span", "c-meta__type").get_text() == article_type
        ]

        save_article(url, translated, articles, n)

    print("Saved all articles.")


def save_article(domain, translation, articles, n):
    # Loop through the articles and save them
    for article in articles:
        r = requests.get(f"{domain}{article.find('a')['href']}")
        soup = BeautifulSoup(r.content, "html.parser")
        path = os.path.join(f"Page_{n}", f"{soup.find('h1').text.translate(translation)}.txt")
        write_content_to_file(path, soup)


def write_content_to_file(path, content):
    # Write the content to the file
    with open(path, "wb") as f:
        text = content.find("div", "c-article-body").text.strip().encode()
        f.write(text)


if __name__ == "__main__":
    main()
