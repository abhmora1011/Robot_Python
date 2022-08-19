def new_game():
    # pass
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-----------------------")
        print(key) # this will print the question in options 2D list
        for i in options[question_num-1]: # Getting the keys which is the questions
            print(i) # This will print the choices
        guess = input("Enter (A, B, C, or D): ").upper()
        guesses.append(guess) # It appends the value entered to the guesses list

        correct_guesses += check_answer(questions.get(key), guess) # value will be added from check_answer() method and evaluate the answers
        question_num += 1

    display_score(correct_guesses, guesses)
# --------------------------
def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0
# --------------------------
def display_score(correct_guesses, guesses):
    print("---------------------------")
    print("RESULTS")
    print("---------------------------")
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ") # Fetching the value of questions and not the key
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ") # Fething the values of guesses
    print()

    score = ((correct_guesses/len(questions))*100) # To get the percentage score
    print("Your score is: " + str(score) + "%")

# --------------------------
def play_again():
    response = input("Do you want to play again? (yes/no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False
# --------------------------

questions = {
    "Who created Python?: ": "A",
    "What year was Python created?: ": "B",
    "Python is tributed to which comedy group?: ": "C",
    "Is the Earth round?: ": "A"
}

options = [
    ["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
    ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
    ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
    ["A. True", "B. False", "C. Sometimes", "D. What's Earth?"]
]

new_game() # initiate the game

while play_again():
    new_game()

print("Bye!")