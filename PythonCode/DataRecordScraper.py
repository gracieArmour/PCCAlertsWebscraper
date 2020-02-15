import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime


# passing arguments from command line to variables
url_to_check = "https://alert.pcc.edu"
sleep_time = 24 * 60 * 60 # 24 hours in seconds

# scraper, grabs webpage only
def scrape(url):
    
    page = requests.get(url)
    
    if page.status_code==200:
        pageStatus = "Page Accessed!"
        soup = BeautifulSoup(page.content, 'html.parser')
        divs = soup.find_all('div')
        statusContainer = divs[2]
        pTags = statusContainer.find_all('p')
        statusText = pTags[2].get_text()
        print(statusText)
    else:
        pageStatus = f"Error code: {page.status_code}, page not accessible"
        statusText = "Page was not accessed, no text retrieved"
    print(pageStatus)
    return pageStatus, statusText

# run always, check once per day
while True:
    timestamp = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    status, text = scrape(url_to_check)
    
    with open("record.txt", "a+") as file_object:
        # Move read cursor to the start of file.
        file_object.seek(0)
        # If file is not empty then append '\n'
        data = file_object.read(100)
        if len(data) > 0 :
            file_object.write("\n")
            file_object.write("\n")
            # Append text at the end of file
        file_object.write(timestamp)
        file_object.write("\n")
        file_object.write(status)
        file_object.write("\n")
        file_object.write(text)
    
    time.sleep(sleep_time) # pauses the program here for sleep_time seconds
