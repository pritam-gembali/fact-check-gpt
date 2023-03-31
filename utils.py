from bs4 import BeautifulSoup
import requests
import re


def getBodyAndText(url):

    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")
    
    title = soup.find("title").text

    # Find the article body using regular expressions and BeautifulSoup
    article_body = soup.find("div", {"class": re.compile("body|content|article")})

    # Extract the text from the article body by finding all the <p> tags inside it
    article_text = ""
    if article_body is not None:
        paragraphs = article_body.find_all("p")
        for paragraph in paragraphs:
            article_text += paragraph.text.strip() + "\n"

    # Print the extracted article text
    print(article_text)
    return { article_text, title }





