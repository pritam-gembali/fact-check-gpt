from bs4 import BeautifulSoup
import requests
import re
import openai
import streamlit as st
import time
from serpapi import GoogleSearch

from langchain import PromptTemplate, LLMChain
from langchain.llms import OpenAI
from selenium import webdriver

llm = OpenAI(model_name="text-davinci-003")

def getBodyAndText(url):

    agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
    # response = requests.get(url, headers=agent)
    driver = webdriver.Firefox()
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html)
    
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
		model= "gpt-4",#gpt-3.5-turbo", 
		messages=[{
			"role": "user", 
			"content": input_text
		}],
		temperature=0.0,
	)
	return results['choices'][-1]['message']['content']

def summarise_page(title, body):
    template = """
                Summarise
                stick to title. Ttile: {title}
                Content: {body}
                """
    # st.write(title, body)

    prompt = PromptTemplate(
        template=template,
	    input_variables=['title','body']
    )

    llm_chain = LLMChain( 
			prompt=prompt,
	  		llm=llm 
		)
    
    return llm_chain.run(title=title,body=body)

def classifyOpposing(claim, searchResult):
    template = """
                Check how aligned are the claim and searchResult.
                claim: {claim}
                searchResult: {searchResult}
                Give me a score in between 1 to 10.
                """
    # st.write(title, body)

    prompt = PromptTemplate(
        template=template,
	    input_variables=['claim','searchResult']
    )

    llm_chain = LLMChain( 
			prompt=prompt,
	  		llm=llm 
		)
    
    return llm_chain.run(claim=claim,searchResult=searchResult)



