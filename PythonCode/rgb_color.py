import pyfirmata


def rgb_color(led,color=[0,0,0]):
    global led_list
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

