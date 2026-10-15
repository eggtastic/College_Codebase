import numpy as np

print("[DATE: 10/13/26]" + "\nNUMPY VER: " + np.__version__) # displays date and NumPy version

print("-"*50) # space

np1 = np.array([6, 9, 6, 7, 4, 2, 0]) # creates a 1D array
for x in np1: # visits each element in the array
    print(x, end=" ") # prints elements on the same line
# output: 6 9 6 7 4 2 0

print("\n" + "-"*50) # space

np1 = np.array([[6, 9, 6], [4, 2, 0]]) # creates a 2D array
for i in np1: # visits each row in the array
    for y in i: # visits each element in the current row
        print(y, end=" ") # prints elements on the same line
# output: 6 9 6 4 2 0

print("\n" + "-"*50) # space

for x in np.nditer(np1): # visits every element in the array
    print(x, end=" ") # prints each element on the same line
# output: 6 9 6 4 2 0

print("\n" + "-"*50) # space

array = np.array([[6, 9, 6], [4, 2, 0]]) # creates a 2D array
for row in range(len(array)): # rows in array length
    for col, value in enumerate(array[row]): # cols inside row
        array[row, col] = 888 # changes each element to 888
print(array) # displays the modified array
"""
output:
[[888 888 888]
 [888 888 888]]
"""

print("-"*50) # space

array = np.array([[6, 9, 6], [4, 2, 0]]) # creates a 2D array
for x in np.nditer(array, op_flags=['readwrite']): # allows modification of elements
    x[...] = x * 2 # doubles each element
print(array) # displays the modified array
"""
output:
[[12 18 12]
 [ 8  4  0]]
"""

print("-"*50) # space

for i, x in enumerate(np.nditer(array, op_flags=['readwrite'])): # tracks each element's index
    if i == 0 or i == array.size - 1: # checks if the element is first or last
        x[...] = x * 2 # doubles only the first and last elements
print(array) # displays the modified array
"""
output:
[[24 18 12]
 [ 8  4  0]]
"""

print("-"*50) # space

array1 = np.array([1, 2, 3]) # creates the first array
array2 = np.array([4, 5, 6]) # creates the second array
for x, y in np.nditer([array1, array2]): # visits corresponding elements in both arrays
    print(f"{x} + {y} = {x + y}") # adds and displays each pair
"""
output:
1 + 4 = 5
2 + 5 = 7
3 + 6 = 9
"""

print("-"*50) # space

color_list = [] # creates an empty list for colors
while True: # repeats until the user stops
    color = input("Enter a color (type 'x' to stop): ") # asks for a color
    if color.lower() == "x": # checks if the user entered x
        break # ends the loop
    color_list.append(color) # adds the color to the list

color_array = np.array(color_list) # converts the list into a NumPy array
print("Colors in the Array:") # displays the heading
print(color_array) # displays the array
"""
sample output:
Enter a color (type 'x' to stop): greem
Enter a color (type 'x' to stop): yellow
Enter a color (type 'x' to stop): x
Colors in the Array:
['greem' 'yellow']
"""

print("-"*50) # space

color = np.array(["Green", "Red", "Yellow"]) # creates an array of colors
frequency = np.array([40, 20, 12]) # creates an array of frequencies
pair = zip(color, frequency) # pairs each color with its frequency
print(type(pair)) # displays the type of object returned by zip()
for color, frequency in zip(color, frequency): # unpacks each color-frequency pair
    print(f"There are {color} in {frequency} frequencies.") # displays each pair
"""
output:
<class 'zip'>
There are Green in 40 frequencies.
There are Red in 20 frequencies.
There are Yellow in 12 frequencies.
"""

print("-"*50) # space

names = ["Alice", "Bob", "Charlie"] # creates a list of names
ages = [25, 30, 35] # creates a list of ages
zipped = zip(names, ages) # pairs each name with an age
print(list(zipped)) # converts the zip object into a list
"""
output:
[('Alice', 25), ('Bob', 30), ('Charlie', 35)]
"""

print("-"*50) # space

names = ["Alice", "Bob", "Charlie"] # creates a list of names
ages = [25, 30, 35] # creates a list of ages
cities = ["New York", "Los Angeles", "Chicago"] # creates a list of cities
zipped = zip(names, ages, cities) # combines corresponding elements into tuples
print(list(zipped)) # displays the list of tuples
"""
output:
[('Alice', 25, 'New York'), ('Bob', 30, 'Los Angeles'), ('Charlie', 35, 'Chicago')]
"""

print("-"*50) # space

zipped = [('Alice', 25), ('Bob', 30), ('Charlie', 35)] # creates a list of paired tuples
names, ages = zip(*zipped) # separates the tuples into names and ages
print(names) # displays the names
print(ages) # displays the ages
"""
output:
('Alice', 'Bob', 'Charlie')
(25, 30, 35)
"""

print("-"*50) # space

names = np.array(["Alice", "Bob", "Charlie"]) # creates a NumPy array of names
ages = np.array([25, 30, 35]) # creates a NumPy array of ages
paired = zip(names, ages) # pairs each name with an age
name, age = zip(*paired) # separates the pairs into names and ages
print(name, age) # displays both tuples
"""
output:
(np.str_('Alice'), np.str_('Bob'), np.str_('Charlie')) (np.int64(25), np.int64(30), np.int64(35))
"""

print("-"*50) # space

names = np.array(["Alice", "Bob", "Charlie"]) # creates a NumPy array of names
ages = np.array([25, 30, 35]) # creates a NumPy array of ages
paired = list(zip(names, ages)) # stores the pairs in a list
for x in paired: # visits each pair in the list
    print(x) # displays the current pair
name, age = zip(*paired) # separates the pairs into names and ages
print(name, age) # displays both tuples
"""
output:
(np.str_('Alice'), np.int64(25))
(np.str_('Bob'), np.int64(30))
(np.str_('Charlie'), np.int64(35))
(np.str_('Alice'), np.str_('Bob'), np.str_('Charlie')) (np.int64(25), np.int64(30), np.int64(35))
"""

print("-"*50) # space

names = np.array(["Alice", "Bob", "Charlie"]) # creates a NumPy array of names
ages = np.array([25, 30, 35]) # creates a NumPy array of ages
combined_info = [f"{name} is {age} years old" for name, age in zip(names, ages)] # creates a sentence for each pair
myNumpy_combined_info = np.array(combined_info) # converts the list into a NumPy array
print(combined_info) # displays the Python list
print(type(combined_info)) # displays the list's type
print(myNumpy_combined_info) # displays the NumPy array
print(type(myNumpy_combined_info)) # displays the array's type
"""
output:
['Alice is 25 years old', 'Bob is 30 years old', 'Charlie is 35 years old']
<class 'list'>
['Alice is 25 years old' 'Bob is 30 years old' 'Charlie is 35 years old']
<class 'numpy.ndarray'>
"""

print("-"*50) # space

names = [] # stores student names
scores = [] # stores student scores

for i in range(5): # repeats five times
    name = input(f"Enter name {i+1}: ") # asks for a student's name
    score = int(input(f"Enter score for {name}: ")) # asks for and converts the score to an integer
    names.append(name) # adds the name to the list
    scores.append(score) # adds the score to the list

data = np.array([(name, score) for name, score in zip(names, scores)], dtype=object) # creates an array of name-score pairs
print("\nContent of the NumPy array:") # displays the heading
for name, score in data: # visits each name-score pair
    print(f"Name: {name}, Score: {score}") # displays the student's name and score

average_score = np.mean(scores) # calculates the average score
highest_score = np.max(scores) # finds the highest score
lowest_score = np.min(scores) # finds the lowest score
highest_index = np.argmax(scores) # finds the index of the highest score
lowest_index = np.argmin(scores) # finds the index of the lowest score
highest_scorer = names[highest_index] # retrieves the highest scorer's name
lowest_scorer = names[lowest_index] # retrieves the lowest scorer's name

print(f"\nAverage score of all students: {average_score:.2f}") # displays the average to two decimal places
print(f"Highest score: {highest_score} (by {highest_scorer})") # displays the highest score and student's name
print(f"Lowest score: {lowest_score} (by {lowest_scorer})") # displays the lowest score and student's name
"""
sample output:
Enter name 1: Alice
Enter score for Alice: 90
Enter name 2: Bob
Enter score for Bob: 85
Enter name 3: Charlie
Enter score for Charlie: 95
Enter name 4: David
Enter score for David: 80
Enter name 5: Eve
Enter score for Eve: 88

Content of the NumPy array:
Name: Alice, Score: 90
Name: Bob, Score: 85
Name: Charlie, Score: 95
Name: David, Score: 80
Name: Eve, Score: 88

Average score of all students: 87.60
Highest score: 95 (by Charlie)
Lowest score: 80 (by David)
"""

print("-"*50) # space