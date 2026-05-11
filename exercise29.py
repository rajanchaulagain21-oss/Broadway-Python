#number guessing game

import random
answer = int(random.randint(1,100))
guesses = 0

while True:
    guess = input("Enter a number between 1 and 100: ")
    guesses += 1
    if guess.isdigit():
        if int(guess) == answer :
            print("!! Congratulation !! You are correct")
            break
        elif int(guess) < answer:
            print("answer is higher.")
        elif int(guess) > answer:
            print("answer is lower.")
        
    else:
        print("invalid number")
    



print(f"no of guesses : {guesses}")
 

