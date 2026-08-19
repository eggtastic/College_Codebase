loop = False
total_score = 0

print("=== Student Performance Analyzer ===")

while loop == False:
    name = input("\nStudent Name: ")
    quiz_no = int(input("Number of Quizzes: "))
    if quiz_no <= 0:
        print("\nInvalid! Enter a positive number.\n")
        quiz_no = int(input("Number of Quizzes: "))
    else:
        pass
    for i in range(1, quiz_no+1):
        quiz_loop = False
        while quiz_loop == False:
            quiz_score = int(input(f"Enter Quiz No. {i}: "))
            if quiz_score <= 100 and quiz_score > 0:
                quiz_loop =  True
            else:
                print("INVALID INPUT: Score must be 0-100.")
                continue
        total_score+=quiz_score

    average_score = total_score / quiz_no

    if average_score >= 75:
        remark = "Passed."
    else:
        remark = "Failed."

    print("----- RESULT -----")
    print("Student Name:", name)
    print("Total:", total_score)
    print("Average:", average_score)
    print("Remark:", remark)

    yesno = input("\nEnter another student? (y/n): ")
    lower_yesno = yesno.lower()

    if lower_yesno == "y":
        continue
    elif lower_yesno == "n":
        loop = True
    else:
        print("INVALID INPUT!")
        break

print("\nProgram Ended. Thank you!")