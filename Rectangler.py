#Rectangle Generator
print("----------Rectangle Generator----------")
exit_flag = "none"
while exit_flag != "":
    rows = "none"
    columns = "none"
    
    #input rows and columns, only allowing digits
    while not rows.isdigit():
        rows = input("How many rows? ")
    while not columns.isdigit():
        columns = input("How many columns? ")
    symbol = input("What symbol to use? ")
    
    #typecasting
    rows = int(rows)
    columns = int(columns)
    
    for x in range(rows):
        print()
        for y in range(columns):
            print(symbol, end="")
    print()
    #exit menu
    exit_flag= input("""
    Press Enter to exit
    or enter any key to generate another rectangle """)
