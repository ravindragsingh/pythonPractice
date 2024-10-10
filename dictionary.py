# Unlike lists or tuples, dictionaries do not store items in a particular order
# Creating a dictionary
# Student dictionary
student = {
    "name": "Emily",
    "age": 22,
    "courses": ["Math", "Science", "History"]
}

# Adding a new key-value pair
student["GPA"] = 3.8

# Modifying an existing value
student["age"] = 23

# Accessing values
print("Student Name:", student["name"])  # Output: Student Name: Emily
print("Courses:", student["courses"])    # Output: Courses: ['Math', 'Science', 'History']

# Checking if a key exists
if "GPA" in student:
    print("GPA is:", student["GPA"])  # Output: GPA is: 3.8


'''
Big O Notation Time Complexity Chart (from best to worst):
O(1) - Constant
O(log n) - Logarithmic
O(n) - Linear
O(n log n) - Log-linear
O(n²) - Quadratic
O(2ⁿ) - Exponential
O(n!) - Factorial
Example Applications of Big O Notation:
Array Access: O(1) - Accessing an element by index in an array.
Array Search: O(n) - Searching an unsorted array for a specific element.
Binary Search: O(log n) - Searching a sorted array.
Bubble Sort: O(n²) - A sorting algorithm with nested loops.
Merge Sort: O(n log n) - Efficient sorting algorithm.
Fibonacci (Recursive): O(2ⁿ) - Exponential growth for recursive algorithms without optimization.
Summary of Big O:
O(1): Fast and efficient for small tasks.
O(n): Grows linearly with the input size.
O(log n): Grows very slowly, ideal for large data sets.
O(n log n): Acceptable for most sorting tasks.
O(n²): Not suitable for large data due to quadratic growth.
O(2ⁿ) / O(n!): Extremely inefficient, avoid if possible.
'''
