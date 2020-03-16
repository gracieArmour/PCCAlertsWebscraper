# all user defined functions needed to run the program are here to keep the program file that communicates with the Arduino neat and consise.
import requests
from bs4 import BeautifulSoup
import pyfirmata


# webscraper, grabs webpage and finds desired alert text
def scrape(url):
    
    try:
        page = requests.get(url)
    
        if page.status_code==200:
            pageStatus = "Page Accessed!"
            soup = BeautifulSoup(page.content, 'html.parser')
            tags = [str(tag) for tag in soup.find_all()]
            for i,content in enumerate(tags):
                if ("h3" in content.lower()):
                    while not('div' in tags[i]):
                        statusTag = tags[i]
                        if not('statusText' in locals()):
                            statusText = statusTag.split('>')[1].split('<')[0]
                        else:
                            statusText = statusText+" "+statusTag.split('>')[1].split('<')[0]
                        i += 1
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


# processing of data to check and interpret status
def status_check(para):
    
    paragraph = para.lower() # it is converted to all lower case since there are some random capitalizations 
    
    campuses = {'pcc':'red','centers':'red', 'campuses':'red', 'cascade':'blue', ' ca ':'blue', 'sylvania':'green', ' sy ':'green', ' syl ':'green', 'south east':'yellow', ' se ':'yellow', 'rock creek':'purple', ' rc ':'purple'}
    # This is the dictionary used for campuses. Each campus has a correspodning color that tells the LED which color it should shine.
    for i in campuses:  
        # i goes through the dictionary and see if it matches any words from the paragraph
        if i in paragraph:
            campus_status = campuses[i]
            # Once it finds a match, colour is assigned the keyword which will be the color for the LED.
    if not('campus_status' in locals()):
        campus_status = "white"
    print(campus_status)
    

    alert = {'It is now safe to resume normal activities':'green','open and observing normal operating hours':'green','restored':'green','outage':'cyan','emergency':'red','emergencies':'red','seek shelter':'red','evacuation':'red','evacuate':'red','evacuated':'red','evacuating':'red','drill':'purple','closed':'yellow','close':'yellow','closing':'yellow','closure':'yellow','cancel':'yellow','cancelled':'yellow','during an emergency':'green'}
    for i in alert:
        if i in paragraph:
            alert_status = alert[i]
        elif 'not a drill' in paragraph:
            alert_status = 'red'
            # this line of code is used to differentiate the line 'not a drill' and 'drill'.
    if not('alert_status' in locals()):
        alert_status = "white"
    print(alert_status)
    
    
    weather = {'wind':'green','winds':'green', 'storm':'purple','storms':'purple','lighting':'yellow','thunder':'yellow','snow':'blue','snowfall':'blue','ice':'blue','icy':'blue','earthquake':'cyan','earthquakes':'cyan','fire':'red','fires':'red'}
    for i in weather:    
        if i in paragraph:
            weather_status = weather[i] 
    if not('weather_status' in locals()):
        weather_status = "white"
    print(weather_status)
    
    
    return campus_status, alert_status, weather_status


# rgb LED color control function for ease of use in final program file
def set_led(led,color=[0,0,0]):
    if not('led_list' in globals()):
        global led_list
        led_list = []
    
    if not(led in led_list):
        led_list.append(led)
    
    colorValue = {'red':[255,0,0],'green':[0,255,0],'blue':[0,0,255],'yellow':[255,255,0],'cyan':[0,255,255],'purple':[255,0,255],'white':[255,255,255]}
    
    for LED_name in globals():
            if globals()[LED_name]==led:
                thisLED = LED_name
                break
            else:
                continue
    
    if type(color)==str:
        try:
            rgb_list = colorValue[color]
        except KeyError:
            print("Invalid color name \""+color+"\" for "+thisLED)
            rgb_list = [255,255,255]
    
    elif type(color)==list:
        rgb_list = color
        place = ['Red','Green','Blue']
        for index, value in enumerate(rgb_list):
            if (value>255) or (value<0):
                print(place[index]+" color value \""+str(rgb_list[index])+"\" is out of range (0 to 255) for "+thisLED)
                rgb_list = [255,255,255]
            else:
                continue
        
    else:
        print("Invalid color format \""+str(type(color)).split('\'')[1]+"\" for "+thisLED)
        rgb_list = [255,255,255]
    
    led[0].write(rgb_list[0]/255)
    led[1].write(rgb_list[1]/255)
    led[2].write(rgb_list[2]/255)
