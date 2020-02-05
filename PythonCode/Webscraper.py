import requests
from bs4 import BeautifulSoup


# getting url from user input
url = input("URL to check: ")


# scraper, grabs webpage only
def scrape():
    
    global url
    
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    if page.status_code==200:
        print("Page Accessed!")
        #print("Contents: "+str(soup))
    else:
        print("Error code: " + str(page.status_code) + " Page not accessible")
    return soup

