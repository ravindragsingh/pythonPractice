#adding different variable types is not possible in python
x = 1
y = "Ravindra"
z = 1j

print(str(x)+y+str(z))


#removing duplicates
mylist = ["a", "b", "a", "c", "c"]
#convert it into dictionary and convert it into list
mylist = list(dict.fromkeys(mylist))
print(mylist)


#reversing a string using function
def my_function(x):
  return x[::-1]

mytxt = my_function("I wonder how this text looks like backwards")

print(mytxt)

#adding 2 numbers
a = input("Type a number: ")
b = input("Type another number: ")

sum = int(a) + int(b)

print("The sum is: ", sum)

print(5/0)

