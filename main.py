from utils import *

# get input URL
url = st.text_area("Enter url","")

if st.button("Submit"):

    # CRAWL the source page : Get body and title of input article
    bodyAndText = getBodyAndText(url)

    # Get summary of the article
    summaryOfInput = summarise_page(bodyAndText["title"],bodyAndText["article_text"])
    st.write(summaryOfInput)

    # Get credibility of article
    credibility = getCredibility(bodyAndText["title"]+"\n"+bodyAndText["article_text"])
    #print(credibility)
    try:
      st.json(credibility)
    except:
      st.json(fix_json(credibility))

    # Get opposing summary
    opposingSummary = getOpposingSummary(summaryOfInput)


    params = {
      "q": summaryOfInput,
      "location": "Bengaluru",
      "hl": "en",
      "gl": "us",
      "google_domain": "google.com",
      "api_key": "d15751e7ca31eacee5c55a58d322c47394e05d4610ccaf7c37bf30c829c2aff4"
    }

    search = GoogleSearch(params)
    results = search.get_dict()['organic_results']
    # st.json(results)
    st.write("Relevant articles")
    relevant_urls = {}
    results = results[0:3]
    index = 0
    for idx in results:
      try:
          matchedBodyAndText = getBodyAndText(idx["link"])
          idx["article_text"] = matchedBodyAndText["article_text"]
          idx["title"] = matchedBodyAndText["title"]
          hitSummary = summarise_page(idx["title"],idx["article_text"])

          # verdict = classifyOpposing(summaryOfInput,hitSummary)
          # objectivity = objectivityAnalysis()
          st.write("-----------------------")
          st.write(idx["link"])
          st.write(idx["title"])
          st.write(hitSummary)
          st.write(verdict)
          st.write("------------------------")
          index = index + 1
      except:
          continue
      
    params = {
      "q": opposingSummary,
      "location": "Bengaluru",
      "hl": "en",
      "gl": "us",
      "google_domain": "google.com",
      "api_key": "d15751e7ca31eacee5c55a58d322c47394e05d4610ccaf7c37bf30c829c2aff4"
    }

    search = GoogleSearch(params)
    print(search.get_dict())
    results = search.get_dict()['organic_results']
    
    # st.json(results)
    st.write("Opposing articles")
    results = results[0:3]
    relevant_urls = {}
    index = 0
    for idx in results:
      try:
          matchedBodyAndText = getBodyAndText(idx["link"])
          idx["article_text"] = matchedBodyAndText["article_text"]
          idx["title"] = matchedBodyAndText["title"]
          hitSummary = summarise_page(idx["title"],idx["article_text"])

          # objectivity = objectivityAnalysis()
          st.write("-----------------------")
          st.write(idx["link"])
          st.write(idx["title"])
          st.write(hitSummary)
          st.write("------------------------")
          index = index + 1
      except:
          continue

