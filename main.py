from utils import *

# get input URL
url = st.text_area("Enter url","")

if st.button("Submit"):

    # CRAWL the source page : Get body and title of input article
    bodyAndText = getBodyAndText(url)

    # Get summary of the article
    summaryOfInput = summarise_page(bodyAndText["title"],bodyAndText["article_text"])
    st.write(summaryOfInput)

    # Get search results based on summary
    """
    TO-DO: CRAWL all results and summarise
    """

    params = {
      "q": summaryOfInput,
      "location": "Bengaluru",
      "hl": "en",
      "gl": "us",
      "google_domain": "google.com",
      "api_key": "e03c16e2e143704e74cbceb5fe64a6013f84a2df6efa9df93d07112c485cfe1e"
    }
    
    search = GoogleSearch(params)
    results = search.get_dict()['organic_results']
    # st.json(results)
    st.write("Relevant snippets")
    relevant_urls = {}
    for idx in results:
        print(idx)
        matchedBodyAndText = getBodyAndText(idx["link"])
        idx["article_text"] = matchedBodyAndText["article_text"]
        idx["title"] = matchedBodyAndText["title"]
        verdict = classifyOpposing(bodyAndText["article_text"], matchedBodyAndText["article_text"])

        st.write(matchedBodyAndText["article_text"],verdict)

    # Classify for and against


    # Get opposing summary, crawl articles
    # Design choice: Whether to get summary or not



    

