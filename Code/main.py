import SHA256Encription; 

print ("------ All Avaible Methods -----")
print ("1.) SHA256 ")
print(" ---------- ")

Choice = int(input("Enter the number of method, that you want: "))

if Choice == 1:
    print("Ok")
    print("--------------------")
    print("1.) Encription")
    print("2.) Decription")
    print("--------------------")
    FinalChoice = int(input("Enter the number of function, that you want: "))
    if FinalChoice == 1:
        SHA256Encription.encript()
    elif FinalChoice == 2:
        SHA256Encription.decript()
    else: print("There is no such a function on that number.. ")
else:
    print("There is no such method, on that number..")

print("That is all! ")
print("Press enter to excape")
Exit = input() 
