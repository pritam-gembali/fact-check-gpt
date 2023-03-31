import streamlit as st
from serpapi import GoogleSearch
from utils import *

url = st.text_area("Enter url","")

if st.button("Submit"):

    # Get body and title of input article
    bodyAndText = getBodyAndText(url)


    # Get summary of the article
    summaryOfInput = parse_with_gpt(bodyAndText["title"]+"\n"+bodyAndText["article_text"])

    st.write(summaryOfInput)

# params = {
#   "q": query,
#   "location": "Bengaluru",
#   "hl": "en",
#   "gl": "us",
#   "google_domain": "google.com",
#   "api_key": "e03c16e2e143704e74cbceb5fe64a6013f84a2df6efa9df93d07112c485cfe1e"
# }

# if st.button("Submit"):
#     search = GoogleSearch(params)
#     results = search.get_dict()['organic_results']
#     st.json(results[0])
    # for idx in results:

    #     st.write(results[idx]['title'])
# if st.button("Submit"):
#     search = GoogleSearch(params)
#     results = search.get_dict()['organic_results']
#     # st.json(results)
#     for idx in results:
#         print(idx)
#         st.write(idx['snippet'])
