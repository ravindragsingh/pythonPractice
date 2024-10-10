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

