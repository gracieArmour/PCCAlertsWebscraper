# import the necessary libraries
import pyfirmata
from time import sleep

# import the user-defined function files
import rgb_color
from webscraper import scrape
from checkingfile import status_check

# tell the program what website to scrape from
url_to_check = 'https://jackiearmour.github.io/PCCAlertsWebscraper/'

# store the name of the USB port the Arduino is connected to
portName = '/dev/cu.usbserial-DN02SJR4'

# create the board object in Python
board = pyfirmata.Arduino(portName)

# setup the LEDs by storing their locations. d for digital, a for analogue, pin number, o for ouput, i for input, p for pwm
campusLED = [board.get_pin('d:10:o'),board.get_pin('d:11:o'),board.get_pin('d:12:o')]
closureLED = [board.get_pin('d:6:o'),board.get_pin('d:7:o'),board.get_pin('d:8:o')]
weatherLED = [board.get_pin('d:2:o'),board.get_pin('d:3:o'),board.get_pin('d:4:o')]


try:
    while True:
        # scrape the webpage
        page_status, status_text = scrape(url_to_check)
        
        if page_status=="Page Accessed!":
            campus_status, closure_status, weather_status = status_check(status_text)
        else:
            print("No status to process")
            campus_status = 'white'
            closure_status = 'white'
            weather_status = 'white'
        
        # set the LEDs to the determined colors
        rgb_color.set_led(campusLED,campus_status)
        rgb_color.set_led(closureLED,closure_status)
        rgb_color.set_led(weatherLED,weather_status)

        # pause here for 30 seconds before checking again
        sleep(30)
        
except KeyboardInterrupt:
    print(rgb_color.led_list)
    for LED in rgb_color.led_list:
        rgb_color.set_led(LED)
    print('Program stopped by user')
    raise
