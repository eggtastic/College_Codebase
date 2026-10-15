import random

set1 = set()
set2 = set()
tmp = set() # elem set storage, this is where the user will answer
given_question = "" # to identify which set operations it is

print("-- SETS GAME! --")

while True:
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

## this is for generating sets
for i in range(questions):
    print("")
    set_length = random.randint(0, 10) ## set length
    # the LC version
    set1 = {random.randint(1,11) for n in range(set_length + 1)}
    set2 = {random.randint(1,11) for n in range(set_length + 1)}

    set_question = random.randint(1, 4) ## union, intersection, diff. or symm. diff.
    match(set_question):
        case 1: ## UNION
            given_question = "UNION."
            answer = set1.union(set2)
        case 2: ## INTERSECTION
            given_question = "INTERSECTION."
            answer = set1.intersection(set2)
        case 3: ## DIFFERENCE
            given_question = "DIFFERENCE."
            answer = set1.difference(set2)
        case 4: ## SYMMETRIC DIFFERENCE
            given_question = "SYMMETRIC DIFFERENCE."
            answer = set1.symmetric_difference(set2)

    # generate_question(set_question)
    print(i + 1, "-", given_question)

    # output
    print(set1)
    print(set2)

    user = input("Enter input here: ")

    if user.strip() == "":
        print("INCORRECT: Answer cannot be empty.")

    elif any(char.isalpha() for char in user):
        print("INCORRECT: Letters are not valid elements.")

    else:
        tmp = {int(x.strip()) for x in user.split(",")}

        if tmp == answer:
            print("CORRECT.")
        else:
            print("INCORRECT.")

        print("The answer is:", answer)