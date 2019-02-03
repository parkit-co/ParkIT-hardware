import os
import datetime
import sys
import time
import subprocess
from gpiozero import MotionSensor
import requests
from time import sleep

pir = MotionSensor(4)

while True: #infinite loop
    
    pir.wait_for_motion() #when movement is detected
    print("Motion Detected")
    
    
    script_dir = os.path.dirname(__file__) #current location of file
    os.system('./webcam.sh') #bash script for USB webcam
    currentdate = datetime.datetime.now().strftime("%Y-%m-%d_$H%M") #Date
    rel_path = currentdate + ".jpg"
    abs_file_path = os.path.join(script_dir, rel_path)
    print (abs_file_path) #photo path
    
    
    results = os.popen('./aplr.sh').read() #run OpenALPR Bash script, then convert terminal output to string
    print(results)
    
    
    try:
        license = (results.splitlines()[1]).split()[1] #takes first license plate guess (highest confidence value)
        
    except IndexError:
        print("No license plates detected.") #when a motion detector is not turned on by a car
    else:
        print (license)
        r = requests.post('http://www.homeparkit.com/parking/parkingLot/spot1', data = {'license' : license
                                                                                        'time' : currentdate
                                                                                        'action'  : 'leaving'}) #simple POST request to ParkIT server
        print (r.text)
        

    
