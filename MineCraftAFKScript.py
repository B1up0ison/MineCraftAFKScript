import time
import pydirectinput
seconds = 326 #minecraft day = 650 so run ~half
while True:
        for i in range(seconds,0,-1):
                print(i, "seconds left")
                time.sleep(1) #buffer
        time.sleep(2)
        pydirectinput.moveTo(950,750) #move cursor down to bed on minecraft windowed mode
        time.sleep(2) 
        pydirectinput.rightClick()  #right click on bed to sleep
        time.sleep(7) #rougly amount of time to sleep in bed
