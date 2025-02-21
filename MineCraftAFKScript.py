import time
import pydirectinput
from pynput import keyboard
seconds = 326 #~Half of minecraft day
mundy = True
print("Welcome to AFK Script. Press ' q ' to quit anytime.")

def meow(key):
        global mundy
        try:
                if key.char == 'q':       #if key == q, then let mundy=False which will cause program to stop
                        mundy = False
        except AttributeError:            #needed because if you press escape or any other key then script may break, as ESC is a special key.
                if key.name == "q":
                        mundy = False

listener=keyboard.Listener(on_press=meow) #listener from pynput to listen for keystrokes.
listener.start()

while mundy: #runs while mundy is true
        for i in range(seconds,0,-1):
                print(i, "seconds left")
                time.sleep(1) #buffer
                if not mundy: #if mundy is not set to true
                        print("script terminated")
                        break
        time.sleep(1)
        pydirectinput.moveTo(950,750) #Align cursor to bed
        time.sleep(1) 
        pydirectinput.rightClick()  #Right click on bed sleep
        time.sleep(5) #Amount of time to sleep in bed
