import random

set1 = {}
set2 = {}
given_question = ""
print("-- SETS GAME! --")

while True:
    set_length = random.randint(0, 10) ## set length

    question_input = input("Number of Questions: ")

    # checks questions
    if question_input.isnumeric():
        questions = int(question_input)

        if questions > 1:
            break
        else:
            print("Try again! Number of questions must be greater than 1.")
            continue
    else:
        print("Sorry! Please enter a valid integer.")    

## question logic
def generate_question():
    
    set_question = random.randint(1, 4) ## union, intersection, diff. or symm. diff.?

    match(set_question):
        case 1: ## UNION
            given_question = "UNION."
        case 2: ## INTERSECTION
            given_question = "INTERSECTION."
        case 3: ## DIFFERENCE
            given_question = "DIFFERENCE."
        case 4: ## SYMMETRIC DIFFERENCE
            given_question = "SYMMETRIC DIFFERENCE."

## this is for generating sets
for i in range(questions):

    generate_question()
    print(i + 1, "-", given_question)

    # the LC version
    for i in range(0, set_length):
        set1 = {random.randint(1,11) for n in range(0, set_length + 1)}
    print(set1)
    for i in range(set_length):
        set2 = {random.randint(1,11) for n in range(0, set_length + 1)}
    print(set2)

    test = int(input("Enter input here: "))
