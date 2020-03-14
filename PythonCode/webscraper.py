import requests
from bs4 import BeautifulSoup


# scraper, grabs webpage only
def scrape(url):
    
    try:
        page = requests.get(url)
    
        if page.status_code==200:
            pageStatus = "Page Accessed!"
            soup = BeautifulSoup(page.content, 'html.parser')
            tags = [str(tag) for tag in soup.find_all()]
            for i,content in enumerate(tags):
                if (("current status" in content.lower()) and ("h3" in content.lower())):
                    statusTag = tags[i+1]
                    statusText = statusTag.split('>')[1].split('<')[0]
            if not('statusText' in locals()):
                statusText = "Status Header not found"
        else:
            pageStatus = f"Error code: {page.status_code}, page not accessible"
            statusText = "Page was not accessed, no text retrieved"
    except Exception as e:
        pageStatus = "Connection to page failed. Error: "+repr(e)
        statusText = "Page was not accessed, no text retrieved"
    finally:
        print(pageStatus)
        print(statusText)
        return pageStatus, statusText
