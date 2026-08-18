while True:
    str1 = input("Input String #1: ")
    str2 = input("Input String #2: ")

    same = True
    if not len(str1) == len(str2):
        same = False
    else:
        for x in range(len(str1)):
            if str1[x] != str2[x]:
                same = False

    if same == True:
        print("Your strings are the same")
    else: 
        print("Your strings are different")