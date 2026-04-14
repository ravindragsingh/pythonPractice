#Tuples and dictionaries
#Tuples are more memory efficient, they are immutables: this differenciates tuples with list
# Creating a tuple
person = ("John", 30, "Engineer")

# Accessing elements in a tuple
name = person[0]
age = person[1]
profession = person[2]

print("Name:", name)  # Output: Name: John
print("Age:", age)  # Output: Age: 30
print("Profession:", profession)  # Output: Profession: Engineer

# Attempting to modify the tuple
''' person[1] = 31  # This will raise a TypeError: 'tuple' object does not support item assignment'''

#tuple concatination
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined_tuple = tuple1 + tuple2
print(combined_tuple)  # Output: (1, 2, 3, 4, 5, 6)

#assigning val;ue to tuple
person = ("Alice", 28, "Doctor")
name, age, profession = person
print(name)  # Output: Alice
print(age)  # Output: 28
print(profession)  # Output: Doctor

single_element_tuple = (5,)  # Note the comma
print(type(single_element_tuple))  # Output: <class 'tuple'>


