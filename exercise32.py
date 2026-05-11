import random



data = ['r','p','s']
while True:


    computer = random.choice(data)
    print(computer)
    user = input("Enter a value r,p,s: ").lower()
    if user not in data:
        print("Invalid input choose r, p ,s ")
        continue

    if computer == user:
        print("Tie")
        

    elif (computer == "r" and user == 'p') or (computer == "p" and user == 's') or (computer == "s" and user == 'r'):
        print("You win")

    else:
        print("You lost")

    



