import numpy as np

np.set_printoptions(precision=2, threshold=np.inf, suppress=True) # controls how NumPy displays array values
arr = np.array([[123456.4534, 222.5465, 12345678.123456789], [444, 555, 666]]) # creates a 2D array
print(arr) # displays the array
"""
output:
[[  123456.45      222.55 12345678.12]
 [     444.         555.         666.  ]]
"""

print("-"*50) # space

arr[1, 0] = 888 # changes the element at row 1, column 0
print(arr) # displays the modified array
"""
output:
[[  123456.45      222.55 12345678.12]
 [     888.         555.         666.  ]]
"""

print("-"*50) # space

np1 = np.array([1, 2, 3, -4, 0, 5, 6, 7, -8, 9]) # creates an array
print(np.absolute(np1)) # converts negative values to positive
print(np.exp(np1)) # calculates e raised to each element
print(np.min(np1)) # finds the smallest element
print(np.max(np1)) # finds the largest element
print(np.sqrt(np1)) # calculates square roots; negative values produce nan
"""
output:
[1 2 3 4 0 5 6 7 8 9]
[2.72 7.39 20.09 0.02 1. 148.41 403.43 1096.63 0. 8103.08]
-8
9
[1. 1.41 1.73 nan 0. 2.24 2.45 2.65 nan 3.]
"""

print("-"*50) # space

arr = np.array([1, 2, 3]) # creates a 1D array
new_arr = np.append(arr, [4, 5, 6]) # adds elements to the end
print(new_arr) # displays the new array
"""
output:
[1 2 3 4 5 6]
"""

arr = np.array([[1, 2, 3], [4, 5, 6]]) # creates a 2D array
new_arr = np.append(arr, [[7, 8, 9]], axis=0) # adds a new row
print(new_arr) # displays the new array
"""
output:
[[1 2 3]
 [4 5 6]
 [7 8 9]]
"""

print("-"*50) # space

arr = np.array([[1, 2, 3], [4, 5, 6]]) # creates a 2D array
print(arr) # displays the original array
new_arr = np.append(arr, [[7], [8]], axis=1) # adds a new column
print(new_arr) # displays the new array
"""
output:
[[1 2 3]
 [4 5 6]]
[[1 2 3 7]
 [4 5 6 8]]
"""

arr = np.array([[1, 2], [3, 4]]) # creates a 2D array
print(arr) # displays the array
"""
output:
[[1 2]
 [3 4]]
"""

print("-"*50) # space

arr = np.array([[1, 2], [3, 4]]) # creates a 2D array
new_arr = np.append(arr, [5, 6]) # adds elements and flattens the result
print(new_arr) # displays the 1D array
"""
output:
[1 2 3 4 5 6]
"""

arr = np.array([[1, 2, 3], [4, 5, 6]]) # creates a 2D array
new_arr = np.append(arr, [[7, 8, 9]], axis=0) # adds a new row
print(new_arr) # displays the new array
"""
output:
[[1 2 3]
 [4 5 6]
 [7 8 9]]
"""

print("-"*50) # space

arr = np.array([[1, 2], [3, 4]]) # creates a 2D array
rows = [[5, 6], [7, 8]] # creates two additional rows
print(arr) # displays the original array
"""
output:
[[1 2]
 [3 4]]
"""

print("-"*50) # space

new_arr = np.append(arr, rows, axis=0) # adds two rows to the original array
print(new_arr) # displays the expanded array
"""
output:
[[1 2]
 [3 4]
 [5 6]
 [7 8]]
"""

arr = np.delete(arr, 1, axis=0) # removes the row at index 1
print(arr) # displays the remaining row
"""
output:
[[1 2]]
"""

arr = np.array([
    [10, 20],
    [30, 40],
    [50, 60],
    [70, 80]
]) # creates a 2D array with four rows

new_arr = np.delete(arr, np.s_[::2], axis=0) # removes rows at indices 0 and 2
print(new_arr) # displays the remaining rows
"""
output:
[[30 40]
 [70 80]]
"""

print("-"*50) # space

arr = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
]) # creates a 2D array

new_arr = np.delete(arr, np.s_[1::2], axis=1) # removes columns at indices 1 and 3
print(new_arr) # displays the remaining columns
"""
output:
[[1 3]
 [5 7]]
"""

print(np.sum(arr, axis=0)) # calculates the sum of each column
print(np.sum(arr, axis=1)) # calculates the sum of each row
"""
output:
[ 6  8 10 12]
[10 26]
"""

print("-"*50) # space

np1 = np.array([0, 1, 2, 3, 4, 5]) # creates the original array
np2 = np1.view() # creates a view sharing the original data

print(f"Original NP1 {np1}") # displays the original array
print(f"Original NP2 {np2}") # displays the view

np1[0] = 41 # changes the first element
print(f"Changed NP1 {np1}") # displays the modified original
print(f"NP2 {np2}") # displays the same change
"""
output:
Original NP1 [0 1 2 3 4 5]
Original NP2 [0 1 2 3 4 5]
Changed NP1 [41  1  2  3  4  5]
NP2 [41  1  2  3  4  5]
"""

print("-"*50) # space

np1 = np.array([0, 1, 2, 3, 4, 5]) # creates the original array
np2 = np1 # assigns both variables to the same array

print(f"Original NP1 {np1}") # displays the original array
print(f"Original NP2 {np2}") # displays the same array

np1[0] = 41 # changes the first element
print(f"NP1 {np1}") # displays the modified array
print(f"NP2 {np2}") # displays the same modification
"""
output:
Original NP1 [0 1 2 3 4 5]
Original NP2 [0 1 2 3 4 5]
NP1 [41  1  2  3  4  5]
NP2 [41  1  2  3  4  5]
"""

print("-"*50) # space

np1 = np.array([0, 1, 2, 3, 4, 5]) # creates the original array
np2 = np1.copy() # creates an independent copy

print(f"Original NP1 {np1}") # displays the original array
print(f"Original NP2 {np2}") # displays the copy

np1[0] = 41 # changes the original array
print(f"Changed NP1 {np1}") # displays the modified original
print(f"NP2 {np2}") # the copy remains unchanged

np2[0] = 888 # changes the copied array
print(f"Changed NP1 {np1}") # the original remains unchanged
print(f"NP2 {np2}") # displays the modified copy
"""
output:
Original NP1 [0 1 2 3 4 5]
Original NP2 [0 1 2 3 4 5]
Changed NP1 [41  1  2  3  4  5]
NP2 [0 1 2 3 4 5]
Changed NP1 [41  1  2  3  4  5]
NP2 [888   1   2   3   4   5]
"""

print("-"*50) # space

np1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # creates a 1D array
print(np1) # displays the array
print(np1.shape) # displays the array dimensions
"""
output:
[1 2 3 4 5 6 7 8 9 0]
(10,)
"""

print("-"*50) # space

np2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]]) # creates a 2D array
print(np2) # displays the array
print(np2.shape) # displays the number of rows and columns
"""
output:
[[1 2 3 4 5]
 [6 7 8 9 0]]
(2, 5)
"""

print("-"*50) # space

np3 = np1.reshape(2, 5, 1) # reshapes ten elements into dimensions of 2 by 5 by 1
print(np3) # displays the reshaped array
print(np3.shape) # displays the new dimensions
"""
output:
[[[1]
  [2]
  [3]
  [4]
  [5]]

 [[6]
  [7]
  [8]
  [9]
  [0]]]
(2, 5, 1)
"""

print("-"*50) # space

np5 = np3.flatten() # converts the multidimensional array into 1D
print(np5) # displays the flattened array
print(np5.shape) # displays the new dimensions
"""
output:
[1 2 3 4 5 6 7 8 9 0]
(10,)
"""

print("-"*50) # space

grocery_dtype = np.dtype([ # defines the fields and their data types
    ('item_name', 'U8'), # stores strings up to 8 characters
    ('product_code', 'U5'), # stores strings up to 5 characters
    ('qty', 'i4'), # stores 4-byte integers
    ('price', 'f4') # stores 4-byte floating-point numbers
])

grocery_data = np.array([ # creates structured grocery records
    ('Apples', 'A101', 40, 50.60),
    ('Grapes', 'G102', 50, 255.50),
    ('Oranges', 'O203', 80, 60.02),
    ('Bananas', 'B304', 100, 30.75)
], dtype=grocery_dtype) # applies the defined data types

print(grocery_data) # displays all grocery records
print(grocery_data[0]) # displays the first record
print(grocery_data[1]) # displays the second record
print(grocery_data[2]) # displays the third record
"""
output:
[('Apples', 'A101',  40,  50.6 )
 ('Grapes', 'G102',  50, 255.5 )
 ('Oranges', 'O203',  80,  60.02)
 ('Bananas', 'B304', 100,  30.75)]
('Apples', 'A101', 40, 50.6)
('Grapes', 'G102', 50, 255.5)
('Oranges', 'O203', 80, 60.02)
"""

second_row_first_three_columns = grocery_data[1][['item_name', 'product_code', 'qty']] # selects three fields from the second record
print("\n\n", second_row_first_three_columns) # displays the selected fields
"""
output:
('Grapes', 'G102', 50)
"""

grocery_data[1]['item_name'] = 'XXX' # changes the second record's item name
grocery_data[1]['product_code'] = 'X305' # changes the second record's product code
grocery_data[1]['qty'] = 88 # changes the second record's quantity
print(grocery_data) # displays the updated records
"""
output:
[('Apples', 'A101',  40,  50.6 )
 ('XXX', 'X305',  88, 255.5 )
 ('Oranges', 'O203',  80,  60.02)
 ('Bananas', 'B304', 100,  30.75)]
"""

print("-"*50) # space

grocery_data = np.delete(grocery_data, 1, axis=0) # removes the record at index 1
print(grocery_data) # displays the remaining records
"""
output:
[('Apples', 'A101',  40,  50.6 )
 ('Oranges', 'O203',  80,  60.02)
 ('Bananas', 'B304', 100,  30.75)]
"""