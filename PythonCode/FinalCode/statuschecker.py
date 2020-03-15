def status_check(para):
    
    paragraph = para.lower() # it is converted to all lower case since there are some random capitalizations 
    
    campuses = {'pcc':'red','centers':'red', 'campuses':'red', 'cascade':'blue', ' ca ':'blue', 'sylvania':'green', ' sy ':'green', ' syl ':'green', 'south east':'orange', ' se ':'orange', 'rock creek':'yellow', ' rc ':'yellow'}
    # This is the dictionary used for campuses. Each campus has a correspodning color that tells the LED which color it should shine.
    for i in campuses:  
        # i goes through the dictionary and see if it matches any words from the paragraph
        if i in paragraph:
            campus_status = campuses[i]
            # Once it finds a match, colour is assigned the keyword which will be the color for the LED.
    if not('campus_status' in locals()):
        campus_status = "white"
    print(campus_status)
    

    alert = {'It is now safe to resume normal activities':'green','open and observing normal operating hours':'green','restored':'green','outage':'yellow','emergency':'red','emergencies':'red','seek shelter':'red','evacuation':'red','evacuate':'red','evacuated':'red','evacuating':'red','drill':'purple','closed':'orange','close':'orange','closing':'orange','closure':'orange','cancel':'orange','cancelled':'orange'}
    for i in alert:
        if i in paragraph:
            alert_status = alert[i]
        elif 'not a drill' in paragraph:
            alert_status = 'red'
            # this line of code is used to differentiate the line 'not a drill' and 'drill'.
    if not('alert_status' in locals()):
        alert_status = "white"
    print(alert_status)
    
    
    weather = {'wind':'green','winds':'green', 'storm':'purple','storms':'purple','lighting':'yellow','thunder':'yellow','snow':'blue','snowfall':'blue','ice':'blue','icy':'blue','earthquake':'orange','earthquakes':'orange','fire':'red','fires':'red'}
    for i in weather:    
        if i in paragraph:
            weather_status = weather[i] 
    if not('weather_status' in locals()):
        weather_status = "white"
    print(weather_status)
    
    
    return campus_status, alert_status, weather_status
