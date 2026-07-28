#python stopwatch
import time

startstopwatch = input("Press Enter to start the stopwatch")

stopwatch = 0
while True:
    print("\033[H\033[2J", end="") #clears the screen

    stopwatch += 1

    seconds = stopwatch % 60            
    minutes = (stopwatch//60) % 60
    hours = (stopwatch//3600) 

    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)