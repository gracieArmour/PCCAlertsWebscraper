import requests
from bs4 import BeautifulSoup


# getting url from user input
url = input("URL to check: ")


# scraper, grabs webpage only
def scrape():
    
    global url
    
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    statusContainer = soup.find_all('div')[2]
    pTag = statusContainer.find_all('p')[2]
    statusText = pTag.get_text()
    
    if page.status_code==200:
        print("Page Accessed!")
        print(statusText)
    else:
        print("Error code: " + str(page.status_code) + " Page not accessible")
    return statusText

