#python timer
import time
from playsound3 import playsound 
exit_flag = "None"

#main loop
while not exit_flag == "":
    print("------------Timer------------")
    print("                             ")

    #initializing variables
    hours = "none"
    minutes = "none"
    seconds = "none"
    
    #time input
    while not hours.isdigit():
       hours = input("How many hours? ")
    while not minutes.isdigit():
        minutes = input("How many minutes? ")
    while not seconds.isdigit():
        seconds = input("How many seconds? ")
    
    #typecasting
    seconds = int(seconds)
    minutes = int(minutes)
    hours = int(hours)

    #turning time into seconds so we can iterate
    timer = seconds + (minutes * 60) + (hours * 3600)
    
    #iterate seconds to 0, while printing current time
    for timer in range(timer,0,-1):
        #turning time back to normal format
        seconds = timer % 60            
        minutes = (timer//60) % 60
        hours = (timer//3600) 
        time.sleep(1)
        print("\033[H\033[2J", end="") #clears the screen
        print(f"{hours:02}:{minutes:02}:{seconds:02}")
            

    print("Timer has finished.")   

    #playing sound 3 times
    for x in range(3):
        playsound(r"D:\Files\Documents\CodeFolder\Manual\Timer\timer_done.mp3",block=False)
        time.sleep(2)
    

    print()
    exit_flag = input("Press Enter to exit, or enter any key to set another timer.")