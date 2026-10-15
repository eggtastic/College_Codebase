import pwinput
import numpy as np
import time

print("-" *10, "LED RUNNING LIGHTS " + "-" *10)

while True:
    username = input("Username: ")
    password = pwinput.pwinput(prompt = "Password:", mask="*")

    if username != "Lim" or password != "LIM":
        print("CREDENTIALS INCORRECT! Please type again.")
        continue
    else:
        print("... USER AUTHENTICATION COMPLETE ! ...")
        break

# def print_matrix():
#     print(" ", *range(1, 20, +1))
#     for i, row in enumerate

matrix = np.zeros((6, 20), dtype = str)
# print(matrix)

## LETTER S FOR SHARYL
time.sleep(1)
for i in range(20):
    matrix[0, i] = "S"
    matrix[0, i-1] = "S"
    matrix[0, i-2] = "S"
    matrix[0, i-3] = "S"
    matrix[0, i-4] = ""
    print(matrix)
    time.sleep(0.1)
## LETTER S FOR SAZON
time.sleep(1)
for i in range(20):
    matrix[0, i] = "S"
    matrix[0, i-1] = ""
    print(matrix)
    time.sleep(0.1)
## LETTER L FOR LIM
time.sleep(1)
for i in range(20):
    for x in range(6): # first tail of L
        matrix[x, i] = "L"
        matrix[x, i-1] = ""
    print(matrix)
    time.sleep(0.1)


