import numpy as np

# # arr =np.arange(100)#gives an array of range 100
# # np.array([3,5,6,7,8,9])

# array1=np.array([[2,5,6,7],[3,4,6,7]],dtype='int32')

# print(array1,array1.dtype)
# # print(array1.shape)2 rows 4 colums

# print(np.zeros((4,6)))
# ''' the ouptut of above is 
# [[0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0.]]'''

# print(np.ones(6)) #output [1. 1. 1. 1. 1. 1.]
# print(np.empty(6)) #output [1. 1. 1. 1. 1. 1.]


# slicing

array2 =np.array([5,7,54,33])
print(array2[2:3])

# axis 0 is for columnwise operation and axis 1 is for rowwise operation

# ar=np.array([[1,2,3],[4,5,6]])
# print(ar.sum(axis=0)) #output [5 7 9]
# print(ar.sum(axis=1)) #output [ 6 15]

# dir(np) #to get all the functions of numpy

np1 =np.array([1,2,4,5,6,7,8])

print(np1[2:5]) #output [4 5 6]
print(np1[-3:-1]) #output [6 7]

# slicing with steps
print(np1[1:5:2]) #output [2 5]

# 2D array slicing
np2 =np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

# to print a single element
print(np2[1,2]) #output 7

# slice a 2d array
print(np2[0:1, 1:3]) #output [[2 3]]
print(np2[0:2 , 1:3]) #output [[2 3]  [6 7]]
print(np2[:,0])

'''Certainly! Let's go through the explanations for each of the statements:

1. `print(np2[0:1, 1:3])`:
   - This statement is using slicing to extract a specific subarray from `np2`.
   - `0:1` selects the rows from index 0 (inclusive) to 1 (exclusive), so it selects only the first row.
   - `1:3` selects the columns from index 1 (inclusive) to 3 (exclusive), so it selects columns 1 and 2.
   - The output will be a 1x2 array: `[[2, 3]]`.

2. `print(np2[0:2, 1:3])`:
   - Similar to the first statement, but now it selects the first two rows (`0:2`).
   - The output will be a 2x2 array: `[[2, 3], [6, 7]]`.

3. `print(np2[:, 0])`:
   - This statement selects all rows (`:`) and only the first column (`0`).
   - The output will be a 1D array containing the values from the first column of `np2`: `[1, 5]`.

Remember, in NumPy indexing, the first index refers to rows, and the second index refers to columns. The colon (`:`) is used for slicing, and `[:, 0]` means "all rows from the first column."'''

