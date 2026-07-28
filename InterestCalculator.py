print("Interest Calculator")

#exit flag gives user enough time to read results
#without exit flag user would immediately be met with a new prompt or program would close

exit_flag = "none"

#main loop
while exit_flag != "":
    #intitializing variables
    principal = "none"
    time_period = "none"
    rate = "none"
    invalid = False

#displays option selector
    print("---------------------------------------------------------------")
    interest_type=input("""What would you like to calculate?
                        Simple Interest  : Enter 1
                        Compound Interest: Enter 2 
                        Your choice: """)

    #checks if option is valid
    if not interest_type.isdigit():
        invalid=True

    #only calculates if option is valid
    if not invalid:

        #simple interest
        if int(interest_type)==1:
            #reprompts if input is not a digit
            while not principal.isdigit():
                principal=(input("Please enter your principal amount: $ "))
            while not rate.isdigit():
                rate=(input("Please enter your annual interest rate: %"))
            while not time_period.isdigit():
                time_period=(input("How many years was your money deposited?: "))
                final_amount=(int(principal)*int(time_period)*(int(rate)/100))+int(principal)

        #compound interest
        elif int(interest_type) == 2:
            while not principal.isdigit():
                principal = (input("Please enter your principal amount: $"))
            while not rate.isdigit():
                rate = (input("Please enter your annual interest rate: %"))
            while not time_period.isdigit():
                time_period = (input("How many years was your money deposited?: "))
            final_amount = int(principal) * ((int(rate)/100)+1) ** int(time_period)

        #deals with invalid choice at option selector
        elif int(interest_type) != 1 and int(interest_type) != 2:
            invalid = True

    #invalid error message
    if invalid:
        print("Please choose a valid option")
        
    #Displaying results
    elif not invalid:
        interest = final_amount - int(principal)
        print("---------------Result------------------")
        print(f"After {time_period} years with a rate of %{rate}: ")
        print(f"Your principle amount is: ${int(principal):.2f}")
        print(f"You now have ${final_amount:.2f}")
        print(f"You gained: ${interest:.2f}")
        

    #exit menu
    exit_flag= input("""
    Press Enter to exit
    or enter any key to do another calculation """)