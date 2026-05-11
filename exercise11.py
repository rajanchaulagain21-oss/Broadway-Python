#Validate user input exercise
# 1. Username is no more than 12 characters
# 2. Username must not contain spaces
# 3. Username must not contain digits

user_name = input("Enter your user name: ")
if len(user_name) > 12 and user_name.find(" ")!= -1 and user_name.isdigit() == False:
    print("Username must not be greater than 12 characters")
    print("username must not contain spaces!")
    print("Username mustnot contain digits")

elif len(user_name) > 12:
    print("Username must not be greater than 12 characters")

elif user_name.find(" ")!= -1:
    print("username must not contain spaces!")

elif user_name.isalpha() != True:
    print("Username mustnot contain digits")

else:
    print(f"Welcome {user_name}")

