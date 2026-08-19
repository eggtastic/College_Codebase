# 8/2/26

import types
import pwinput 
# note that BEFORE u even hit run, type "pip install pwinput" for pwinput to WORK
import msvcrt

print("HELLO DATSCI BSCS 2A!")

print("\n" + "-"*10)

# slicing [start : stop]
my_name = "Lynx Deez"
# fn = my_name[0:6], same thing as below
fn = my_name[:4]
ln = my_name[5:9]
print(fn)
print(ln)

# reverse name? [start:stop:step]
rev = my_name[::-1]
print(rev)
rev = my_name[::-2]
print(rev)

#reversed last name, negative means it begins from the right
rev_ln = my_name[:6:-1]
print(rev_ln)

#simpler way to print something multiple times
print("apple"*5)

#so no spaces between seperate print statements
print("a", end="")
print("b", end="")
print("c", end="")

#diff methods to initialize list
#method 1
nums = []
print(nums, type(nums))
#method 2
nums = list
print(nums, type(nums))
#method 3
nums = [50, 50, 420]
print(nums, type(nums))
#method 4 many type
types = [10, "Egg", 50.50, True]
print(types, type(types))

##############
print("\n" + "-" * 5, "DAY 2", "-" * 5)
print("LIST WITHIN RANGE")

numbers = list(range(10, 0, -1)) ## start at 10, end at 1, -1 ensures its reversed
print(numbers) # output: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
five = [5] * 10 ## printing 5 ten times
print(five) # output: [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
matrix = [[0] * 3] * 3 ## printing 0 inside [] three times, three times
print(matrix) # output: [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
matrix[1][1] = 10 ## imagine all of the [0,0,0] ontop of eachother
print(matrix) # output: [[0, 10, 0], [0, 10, 0], [0, 10, 0]]

print("-" * 10)

## LIST COMPREHENSION

print("-- 1 TO 5 --")
# long method: appending numbers from 0 to 5
numbers = []
for i in range(5):
    numbers.append(i)
print(numbers)
# LC
numbers = [i for i in range(5)]
print(numbers)

print("-" * 10)

print("-- SQUARING, 1 TO 5 --")
# long method: squaring numbers from 0 to 5
numbers = []
for i in range(5):
    numbers.append(i**2)
print(numbers)
# LC
numbers = [i**2 for i in range(5)]
print(numbers)

print("-" * 10)

print("-- EVEN ONLY --")
# long method: even numbers only, from 1 to 10
even = []
for x in range(10):
    if x % 2 == 0:
        even.append(x)
print(even)
# LC
even = [x for x in range(10) if x % 2 == 0]
print(even)

print("-" * 10)

print("-- 1 TO 10, BUT ONLY... --")
# displaying num. from 1-10, "yoko" contains what we want to only show
yoko = [5, 10, 15, 20, 2] ## i.e, numbers i want to display
# long method
tmp = [] # "temporary" list
for x in yoko:
    if x <= 10:
        tmp.append(x)
print(tmp)
# LC
tmp = [x for x in yoko if x <= 10]
print(tmp)

print("-" * 10)

print("-- COLUMNS OF [1-5] --")
numbers = []
for row in range(4):
    current_row = []
    for column in range(1, 6):
        current_row.append(column)
    numbers.append(current_row)
print(numbers)
# LC
numbers = [[column for column in range(1, 6)] for row in range(4)]
print(numbers)

print("-" * 10)

print("-- MULTIPLICATION TABLE --")
table = []
for row in range(1, 6):
    current_row = []
    for column in range(1, 6):
        # print(row,"*", column, "=", (row * column))
        current_row.append(row * column)
    table.append(current_row)
print(table)

# LC, note: start reading at the last "for"
table = [[(row * column) for column in range(1, 6)] for row in range(1, 6)]
print(table)

print("-" * 10)

print("-- ODD OR EVEN --")
# system that prints "even" if even, and "odd" if odd

numbers = ["EVEN" if num % 2 == 0 else "ODD" for num in range(1, 11)]
print(numbers)

print("-" * 10)

numbers = [3, 8, 4, 1]
values = [num for num in range(1, 11) if num not in numbers]
print(values)
# how to print 3 more times
values = [[num for num in range(1, 11) if num not in numbers] for num in range(3)]
print(values)
# in reverse
values = [[num for num in range(10, 0, -1) if num not in numbers] for num in range(3)]
print(values)
# + if even say "EVEN"
values = [["EVEN" if num % 2 == 0 else num for num in range(10, 0, -1) if num not in numbers] for num in range(3)]
print(values)

##############
print("\n" + "-" * 5, "DAY 3", "-" * 5)

print("-"*10)

print("-- MASK PASSWORD --")
# import pwinput (this is important; i put this at the very top, but it can be put anywhere)
password = pwinput.pwinput("Password:", mask="*")
print(password)

print("-"*10)

print("-- APPEND()--") # add
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)

print("-"*10)

print("-- INSERT() --")
numbers = [1, 2, 3]
numbers.insert(1,4)
print(numbers)

print("-"*10)

print("-- EXTEND() --") # (to add multiple values)
numbers = [1, 2, 3]
print(numbers)
numbers.extend([4, 5, 6, 7])
print(numbers)

print("-"*10)

print("-- EDIT --")
numbers[1] = 200
print(numbers)
numbers = list(range(1, 6))
print(numbers)
numbers[1:] = [4, 5, 6, 7]
print(numbers)

print("-"*10)

print("-- REMOVE() --")# V1; if the number doesn't exist, there'll be error
numbers = [10, 20, 30, 40, 50]
numbers.remove(30)
print(numbers)

print("-"*10)

print("-- SAFE REMOVE --") #sir's demo, it works even the number is not found
print(numbers)
lst = [10, 20, 30, 40, 50]
def safe_remove(lst, to_remove):
        if to_remove in lst:

            lst.remove(to_remove)
        else:
            print("ERROR: Number doesn't exist.")
        return lst

numbers = safe_remove(lst, 10)
print(numbers)

print("-"*10)

print("-- SPLITTING #2 --")
# #1 was by "[start:stop]"ing, #2 is by calling within an array
complete_name = input("Enter complete name(LN, FN, MN): ").split()
print(complete_name, "FN:", complete_name[1], "MN:", complete_name[2], "LN:", complete_name[0])
#note that because of the order of strings, 0 is last, 1, is first, 2 is middle

print("-"*10)

print("-- MSVCRT --") #stands for "microsoft visual c++ runtime"
# provides standard C library functions compiled w/ microsoft visual c++
password = ""
print("Password:", end="", flush=True)
# "flush" means to IMMEDIATELY show to screen right away
# why use it? it gives the next effect of showing * when typing
while True:
    ch = msvcrt.getwch() # getwch captures input directly w/o pressing enter
    if ch == "\r": # "\r" means ENTER in unicode language
        break
    elif ch == "\b": # this handles backspace
        if password:
            password = password[:-1]
            print("\b \b", end="", flush=True)
    else:
        password += ch
        print("*", end="", flush=True)

print() # this is just an empty space
print(password) # this line will show the password u input

print("-"*10)

print("-- MULTI-LINE TEXT --")
lines = []
print("Enter Letter for PEN PAL (Type 'END' TO SEND...)")
while True:
    line=input()
    if line == "END":
        break
    lines.append(line)
text = "\n".join(lines) # ok wow sir didnt explain join(), but \n means ENTER
# so clicking ENTER won't break the while loop, typing "END" would
print(text)
print("YOUR LETTER: ", lines)

# one last note, i forgot to put pop()
# just know the difference: 
#pop() removes an element from a list by its index and returns that element, while remove() deletes an element by its value and does not return anything. Use pop() when you need the removed item, and use remove() when you only know the value you want to delete.
