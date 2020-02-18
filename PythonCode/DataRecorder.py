import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime


# passing arguments from command line to variables
url_to_check = "https://alert.pcc.edu"
sleep_time = 24 * 60 * 60 # 24 hours in seconds

# scraper, grabs webpage only
def scrape(url):
    
    try:
        page = requests.get(url)
    
        if page.status_code==200:
            pageStatus = "Page Accessed!"
            soup = BeautifulSoup(page.content, 'html.parser')
            tags = [str(tag) for tag in soup.find_all()]
            index = 0
            for i in tags:
                index = index + 1
                if ("Current status" in i):
                    statusTag = tags[index]
                    statusText = statusTag.split('>')[1].split('<')[0]
            if not('statusText' in locals()):
                statusText = "Status Header not found"
        else:
            pageStatus = f"Error code: {page.status_code}, page not accessible"
            statusText = "Page was not accessed, no text retrieved"
    except:
        pageStatus = "Connection to page failed"
        statusText = "Page was not accessed, no text retrieved"
    finally:
        print(pageStatus)
        print(statusText)
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
