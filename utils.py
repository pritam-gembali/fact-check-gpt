from bs4 import BeautifulSoup
import requests
import re
import openai


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
    return { "article_text": article_text, "title": title }

def parse_with_gpt (input_text: str, max_tokens: int = 1500) -> dict:
	"""
		This function utilizes the new gpt-3.5-turbo model that powers chatGPT
		Args: 
			input_text: the input text along with the prompt that we want to pass to GPT
			max_tokens: the maximum number of tokens that we want in the completion
		Returns:
			The JSON data extracted from the text by GPT
	"""

	results = openai.ChatCompletion.create(
		model= "gpt-3.5-turbo", 
		messages=[{
			"role": "user", 
			"content": input_text
		}],
		temperature=0.0,
	)
	return results['choices'][-1]['message']['content']



