'''NumPy (short for Numerical Python) is a powerful Python library used for numerical computing. It provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to perform operations on these arrays efficiently. NumPy is widely used in scientific computing, data analysis, machine learning, and more.'''
import numpy as np

'''creating arrays'''
arr = np.array([1, 2, 3, 4, 5])
print(arr)
# Output: [1 2 3 4 5]

matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix)
# Output:
# [[1 2 3]
#  [4 5 6]]

zeros = np.zeros((2, 3))
print(zeros)
# Output:
# [[0. 0. 0.]
#  [0. 0. 0.]]

ones = np.ones((3, 2))
print(ones)
# Output:
# [[1. 1.]
#  [1. 1.]
#  [1. 1.]]

arange = np.arange(0, 10, 2)
print(arange)
# Output: [0 2 4 6 8]

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print(arr1 + arr2)  # Output: [5 7 9]
print(arr1 * arr2)  # Output: [ 4 10 18]

arr = np.array([1, 2, 3])
print(arr + 5)  # Output: [6 7 8]

#indexing & slicing
arr = np.array([10, 20, 30, 40, 50])
print(arr[2])        # Output: 30
print(arr[1:4])      # Output: [20 30 40]

arr = np.array([1, 2, 3, 4, 5])
print(np.sum(arr))       # Output: 15
print(np.mean(arr))      # Output: 3.0
print(np.max(arr))       # Output: 5
print(np.sqrt(arr))      # Output: [1. 1.41421356 1.73205081 2. 2.23606798]

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(np.dot(A, B))   # Matrix multiplication
# Output:
# [[19 22]
#  [43 50]]

arr = np.array([1, 2, 3, 4, 5, 6])
reshaped = arr.reshape((2, 3))
print(reshaped)
# Output:
# [[1 2 3]
#  [4 5 6]]
