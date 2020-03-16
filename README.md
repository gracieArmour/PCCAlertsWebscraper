# PCCAlertsWebscraper
```A Python/Arduino webscraping project that lights up LEDs based on data from the Portland Community College Alerts system.```

Jackie Armour, Natalia Creagh, Daniel Maestas
Winter ENGR114
3/15/2020
Arduino Predicts Impending Disaster

Problem Statement:

Our group was tasked with web scraping the PCC Alert Page to find alerts and present the alert in the form of an LED’s color change. https://alert.pcc.edu/



Hardware Setup:
Bill of Materials
Part Name
Purpose
Item Name
URL
Price
DEV-13975	
Takes code and installs it into breadboard
SparkFun RedBoard - Programmed with Arduino
https://www.sparkfun.com/products/13975
$  19.95
DEV-11235
Holds Arduino and Breadboard
Arduino and Breadboard Holder
https://www.sparkfun.com/products/11235
$    3.95
CAB-11301
Connects computer to RedBoard
SparkFun USB Mini-B Cable - 6 Foot
https://www.sparkfun.com/products/11301
$    3.95
COM-12062
Indicate alerts
LED - Assorted (20 pack)
https://www.sparkfun.com/products/12062
$    2.95
COM-11507
Reduces current flow
Resistor 330 Ohm 1/6 Watt PTH - 20 pack
https://www.sparkfun.com/products/11507
$    0.95
COM-11508
Reduces current flow
Resistor 10K Ohm 1/6th Watt PTH - 20 pack
https://www.sparkfun.com/products/11508
$    0.95

Hardware Schematic


Hookup Guide
Part
Pin
Connector
Pin
Part
Redboard
GRND
Black Wire
-
Breadboard
Redboard
12
Blue Wire
a28
Breadboard
Redboard
11
Green Wire
a29
Breadboard
Redboard
10
Red Wire
a30
Breadboard
Redboard
8
Blue Wire
a8
Breadboard
Redboard
7
Green Wire
a9
Breadboard
Redboard
6
Red Wire
a7
Breadboard
Redboard
a3
Black Wire
-
Breadboard
Redboard
a25
Black Wire
-
Breadboard
Breadboard
b2
White LED
b3,b4,b5
Breadboard
Breadboard
c5
Resistor
c9
Breadboard
Breadboard
d4
Resistor
d8
Breadboard
Breadboard
e2
Resistor
e7
Breadboard
Breadboard
a24
White LED
b25,b26,b27
Breadboard
Breadboard
c27
Resistor
c30
Breadboard
Breadboard
d26
Resistor
d29
Breadboard
Breadboard
e24
Resistor
e28
Breadboard

Image of hardware all connected:

Code:
Python Code
webscraper.py

import requests




from bs4 import BeautifulSoup












\# scraper, grabs webpage only


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


Arduino Code
MasterProgram.py
\# import the necessary libraries




import pyfirmata


from time import sleep







\# import the user-defined function files


import rgb_color


from webscraper import scrape


from statuschecker import status_check







\# tell the program what website to scrape from


url_to_check = 'https://alert.pcc.edu/' #'https://jackiearmour.github.io/PCCAlertsWebscraper/'







\# store the name of the USB port the Arduino is connected to


portName = '/dev/cu.usbserial-DN02SJR4'







\# create the board object in Python


board = pyfirmata.Arduino(portName)







\# setup the LEDs by storing their locations. d for digital, a for analogue, pin number, o for ouput, i for input, p for pwm


campusLED = [board.get_pin('d:10:o'),board.get_pin('d:11:o'),board.get_pin('d:12:o')]


alertLED = [board.get_pin('d:6:o'),board.get_pin('d:7:o'),board.get_pin('d:8:o')]


weatherLED = [board.get_pin('d:2:o'),board.get_pin('d:3:o'),board.get_pin('d:4:o')]












try:


   while True:


       # scrape the webpage


       page_status, status_text = scrape(url_to_check)


      


       if page_status=="Page Accessed!":


           campus_status, alert_status, weather_status = status_check(status_text)


       else:


           print("No status to process")


           campus_status = 'white'


           alert_status = 'white'


           weather_status = 'white'


      


       # set the LEDs to the determined colors


       rgb_color.set_led(campusLED,campus_status)


       rgb_color.set_led(alertLED,alert_status)


       rgb_color.set_led(weatherLED,weather_status)







       # pause here for 30 seconds before checking again


       sleep(30)


      


except KeyboardInterrupt:


   print(rgb_color.led_list)


   for LED in rgb_color.led_list:


       rgb_color.set_led(LED)


   print('Program stopped by user')


   raise
Results:
The code results in three files with massive functions feeding into one compact file. The arduino code enables the LEDs to light up according to the alert assigned to a color.


Future Work:

What could another group of students do to build on this project? Any resources this group could use to build this future work?

A future group of students could add more LEDs/colors to indicate a wider range of alerts. This would require a larger or multiple redboards because more pins are needed to connect the hardware.
License
MIT License









Copyright (c) 2020 Jackie Armour







Permission is hereby granted, free of charge, to any person obtaining a copy


of this software and associated documentation files (the "Software"), to deal


in the Software without restriction, including without limitation the rights


to use, copy, modify, merge, publish, distribute, sublicense, and/or sell


copies of the Software, and to permit persons to whom the Software is


furnished to do so, subject to the following conditions:







The above copyright notice and this permission notice shall be included in all


copies or substantial portions of the Software.







THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR


IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,


FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE


AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER


LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,


OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE


SOFTWARE.

