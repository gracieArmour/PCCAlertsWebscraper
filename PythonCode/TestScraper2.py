import requests
from bs4 import BeautifulSoup
#import argparse

# grab arguments from command line
#parser = argparse.ArgumentParser(description='Regularly check for a change in the first paragraph tag of a webpage')
#parser.add_argument('webpage', metavar='url', type=str, help='url to check')

#args = parser.parse_args()


# passing arguments from command line to variables
url = "https://www.google.com"


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
    return NULL

# actual prossessing of webpage data into useful info
def magic():
    scrape()
    
    
    return NULL

magic()
