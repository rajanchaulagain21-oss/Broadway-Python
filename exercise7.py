#taking user response on food 
while True:

    response = input("Would you like some food(Y/N)?: ")
    if response.upper() =="Y":
        print("Our waiter will contact you shortly!")

    elif response.upper() == "N":
        print("Thank you for visiting!!")
        break
    else:
        print("please type either Y or N")