# Python Quiz game
questions = ("1. which element is the first element in periodic table?: ",
             "2. Which animal is the largest animal?: ",
             "3. What is the natural satellite of earth?:")
options = (("a. hydrogen","b. helium","c. calcium","d. oxygen"),
           ("a. Whale","b. Elephant","c. Tiger","d. Crocodile"),
           ("a. jupiter","b. moon","c. saturn","d. Mercury"))
answers= ("a","a","b")
question_num= 0
guesses = []
score = 0

for question in questions:
    print("-------------------------")
    print(question)
    
    
    for option in options[question_num]:
        print(option)
    


    guess = input("Enter (a, b, c, d): ").lower()
    guesses.append(guess) 
    if guess == answers[question_num]:
        score += 1
        print("correct") 

    else:
        print("Incorrect")

    question_num += 1
print("----------------")
print("    RESULTS         ")
print("----------------")

print("answers: ", end="")

for answer in answers:
    print(answer, end=" ")

print()

print("Guesses: ", end="")

for guess in guesses:
    print(guess, end=" ")

print()

score = int(score/ len(questions)*100)
print(f"Your score is:{score} %")