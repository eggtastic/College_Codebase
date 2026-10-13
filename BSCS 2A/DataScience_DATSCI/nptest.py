import numpy as np
print(np.__version__)

np1 = np.array([1, 2, 3, 4, 5])
print(np1)
print(np1[2])
print(np1.dtype)

print("")

myList = [1,2,3,4]

np8 = np.array(myList)
print(myList)
print(np8[1])

print("")

np1 = np.array([1, 'apple', 3,4,5])
print(np1[1])
print(np1.dtype, type(np1[1]))