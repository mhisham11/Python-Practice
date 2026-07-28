#This program verifies that username inputed:
# is not empty
# contains only letters
# contains no spaces
# is not longer than 12 characters
invalid= True
while invalid==True:
    username = input("Please enter a username: ")
    #Presence Check
    if bool(username)==False:
        print("Username cannot be empty")
        invalid = True
    if bool(username)==True:
        invalid=False
    #Length Check (Max 12 Characters)
    if len(username) > 12:
        print("Username cannot be longer than 12 characters")
        invalid = True
    #Username must only be letters
    if username.isalpha()==False:
        print("Username must only contain letters")
        invalid = True
    #Username must not contain spaces
    if username.find(" ") != -1:
        invalide = True
        print("Username must not contain spaces")
print("Username has been saved successfully")
#endscreen prevents program from instantly closing upon completion
endscreen = input("Press Enter to exit")