import streamlit as st
from serpapi import GoogleSearch

query = st.text_area("Enter query","")
params = {
  "q": query,
  "location": "Bengaluru",
  "hl": "en",
  "gl": "us",
  "google_domain": "google.com",
  "api_key": "e03c16e2e143704e74cbceb5fe64a6013f84a2df6efa9df93d07112c485cfe1e"
}

if st.button("Submit"):
    search = GoogleSearch(params)
    results = search.get_dict()['organic_results']
    st.json(results[0])
    # for idx in results:

    #     st.write(results[idx]['title'])