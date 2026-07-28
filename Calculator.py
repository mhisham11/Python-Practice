print("Calculator App 2026 Version 12.6")
while 1==1:
    operator = (input("""Choose an operator:
    Multiply : A
    Divide : B
    Subtract: C
    Add : D
    Raise to the power: E
    Your choice: """))
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = operator.upper()
    if operator == "A":
        result = num1*num2
    elif operator == "B":
        result = num1/num2
    elif operator == "C":
        result = num1-num2
    elif operator == "D":
        result = num1+num2
    elif operator == "E":
        result = num1**num2
    else:
        print("Please choose a valid operator.")
        result = "Invalid"
    print(f"Answer: {result}")
    wantround = (input("Do you want to round your answer? (Y/N)"))
    if wantround.upper() == "Y":
        decimals = int(input("How many decimal places to round to?"))
        roundedans = round(result,(decimals))
        print(f"Rounded Answer: {roundedans}")
    print("----Next Calculation----")

