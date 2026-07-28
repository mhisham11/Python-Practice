import random

exit_flag = "None"
count = 0
headcount = 0
tailcount = 0

print("------- Coin Flipper 3000 -------")

#main loop
while exit_flag.lower() != "q":
    
    #reveal input isn't used, it's just there so user can choose when to flip
    reveal = input("Press Enter to flip a coin")

    result = random.randint(1,2)

    if result == 1:
        print ("Result: Heads")
        headcount += 1
    else:
        print ("Result: Tails")
        tailcount += 1
    count += 1

    print(f"------- That was flip #{count} -------")
    print(f"Total results: {headcount} Heads and {tailcount} Tails")

     #exit menu
    exit_flag= input("""
    Enter Q to quit
    Or press Enter to do another flip """)