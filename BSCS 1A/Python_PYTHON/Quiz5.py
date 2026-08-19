names = []
subjects = ("Math", "English", "Science")
grades = {}

options = ["Display All Students and Scores", "Display Average Score", "Display Passed/Failed",
"Delete Student", "Exit"]

print("----- WELCOME -----")

while (True):
    students = int(input("Number of Students: "))
    if students <= 0:
        print("INPUT INVALID. Try again.")
        continue
    else:
        break

for i in range (1, students+1):
    print()

    name = input("Student: ")
    names.append(name)

    grades[name] = {}

    for subject in subjects:
        score = int(input(subject + ": "))
        grades[name][subject] = score

def show_options():
    for i in range(len(options)):
        print((i+1), "-", options[i])

print("\n=== STUDENT RECORD SYSTEM ==\n")

while (True):
    show_options()
    choice = int(input("Enter choice: "))
    match choice:
        case 1:
            print("-- ALL STUDENTS & SCORES --")

            for name in names:
                print()

                print(name + ":")
            
                for subject in subjects:
                    print(subject, "=", grades[name][subject])

        case 2:
            print("-- AVERAGE SCORE --")

            for name in names:
                print()
                total = 0

                for subject in subjects:
                    total = total + grades[name][subject]

                average = total / len(subjects)

                print(name + ":", average)

        case 3:
            print("-- PASSED/FAILED --")

            for name in names:
                print()
                total = 0

                for subject in subjects:
                    total = total + grades[name][subject]

                average = total / len(subjects)

                if average >= 75:
                    print(name + ": PASSED")
                else:
                    print(name + ": FAILED")

        case 4:
            print("-- DELETE STUDENT --")

            name = input("Enter student name to delete: ")

            if name in names:
                names.remove(name)
                del grades[name]
                print("Student deleted.")
            else:
                print("Student not found")
         
        case 5:
            print("-- EXIT --")

            print("PROGRAM ENDED. Thank you for using the system!")
            break

        case _:
            print("INPUT INVALID. Try again.")

    print()