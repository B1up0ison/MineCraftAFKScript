import time
import pydirectinput
seconds = 326 #~Half of minecraft day
while True:
        for i in range(seconds,0,-1):
                print(i, "seconds left")
                time.sleep(1) #buffer
        time.sleep(1)
        pydirectinput.moveTo(950,750) #Align cursor to bed
        time.sleep(1) 
        pydirectinput.rightClick()  #Right click on bed sleep
        time.sleep(5) #Amount of time to slee in bed
