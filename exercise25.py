#Python Quiz Game 
#Who wants to be a millionnare?

questions = (
"1. What is the capital of Nepal?",
"2. Which planet is known as the Red Planet?",
"3. Who wrote Romeo and Juliet?",
"4. What is the largest ocean on Earth?",
"5. Which country is famous for the Eiffel Tower?",
"6. What is the boiling point of water?",
"7. Who is known as the Father of Computers?",
"8. Which gas do plants absorb from the atmosphere?",
"9. Which is the largest continent?",
"10. Who discovered gravity?",
"11. Which is the fastest land animal?",
"12. What is the national flower of Nepal?",
"13. Which country invented pizza?",
"14. How many continents are there?",
"15. What is the currency of Japan?",
"16. Which organ pumps blood in the human body?",
"17. Who painted the Mona Lisa?",
"18. What is the tallest mountain in the world?",
"19. Which language is most spoken worldwide?",
"20. Which animal is known as the King of the Jungle?"
)
options = (
("A. Pokhara", "B. Lalitpur", "C. Kathmandu", "D. Biratnagar"),
("A. Earth", "B. Mars", "C. Venus", "D. Jupiter"),
("A. Charles Dickens", "B. William Shakespeare", "C. Mark Twain", "D. Leo Tolstoy"),
("A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"),
("A. Italy", "B. Germany", "C. France", "D. Spain"),
("A. 90°C", "B. 100°C", "C. 80°C", "D. 120°C"),
("A. Alan Turing", "B. Charles Babbage", "C. Bill Gates", "D. Steve Jobs"),
("A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Hydrogen"),
("A. Africa", "B. Europe", "C. Asia", "D. Australia"),
("A. Albert Einstein", "B. Isaac Newton", "C. Galileo", "D. Nikola Tesla"),
("A. Lion", "B. Tiger", "C. Cheetah", "D. Leopard"),
("A. Rose", "B. Lotus", "C. Rhododendron", "D. Sunflower"),
("A. USA", "B. Italy", "C. France", "D. Greece"),
("A. 5", "B. 6", "C. 7", "D. 8"),
("A. Won", "B. Dollar", "C. Yen", "D. Peso"),
("A. Brain", "B. Liver", "C. Heart", "D. Lungs"),
("A. Pablo Picasso", "B. Leonardo da Vinci", "C. Vincent van Gogh", "D. Michelangelo"),
("A. K2", "B. Kangchenjunga", "C. Mount Everest", "D. Makalu"),
("A. English", "B. Spanish", "C. Mandarin Chinese", "D. Hindi"),
("A. Tiger", "B. Lion", "C. Elephant", "D. Bear")
)
answers = (
"C","B","B","D","C",
"B","B","C","C","B",
"C","C","B","C","C",
"C","B","C","C","B"
)
guesses = []
question_num = 0
score = 0 

for question in questions:
    print("---------------------------")
    print(question)

    for option in options[question_num]:
        print(option)

    guess = input("Enter your guess(A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("correct")
    else:
        print("incorrect")
        print(f"The correct answer is {answers[question_num]}")
    question_num += 1
print("---------------------")
print("      RESULTS     ")
print("---------------------")
print("Guesses:",end=" ")
for guess in guesses:
    print(guess,end=" ")

print()

print("Answers:",end=" ")
for answer in answers:
    print(answer,end=" ")

print()
score = int(score/len(questions)*100)
print(f"Your Score is {score}%")