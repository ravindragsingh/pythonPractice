
#weight conversion program
'''weight = int(input("weight "))
unit = input("enter k for kg and l for lb ")

if unit.upper == "L":
    converted = weight * .45
    print(f"Weight is {converted} lbs")
else:
    converted = weight//2.4
    print(f"Weight is {converted} kilos ")
'''
#guess the number program

'''secret_number = 9
guessCount =0
guessLimit = 3
while guessCount< guessLimit:
    guessNumber = input("Guess the number ")
    guessCount=guessCount+1
    if(int(guessNumber) == int(secret_number)):
        print("You guessed it")
        break
else:
    print("Sorry ! you failed")
'''

#a Game: Start, Stop, Quit
'''
print("Type Start to Start the car")
print("Type Stop to Stop the Car")
print("Type Quit to quit the game")

userInput = ""
started = False
stopped = False
while True:
    userInput = input("What do you want to do ").lower()
    if(userInput == "start"):
        if started:
            print("Car already started")
        else:
            started = True
            stopped = False
            print("Car started")
        #break
    elif(userInput == "stop"):
        if stopped:
            print("Car already stopped")
        else:
            stopped = True
            started = False
            print("Car stopped")
        #break
    elif(userInput == "quit"):
        print("Quitting the game")
        break
    else:
        print("i dont understand")
        #break

        '''

'''
#list - program to print the price of 
prices = [10,20,30]
total = 0
for price in prices:
    #total = total + price
    #print(f"Total = {total}")
    print(f'{price},"GAP"{prices}')

'''
'''
#list & nested loop exercise
patterns = [5,2,5,2,2]
for k in patterns:
    print('x'*k)
    
'''
'''
#list more example
name = ["Ravubdra", "Ravi","Pri","Goldu","Gudiya"]
print(name[1])
print(name[2:])

#updating an item in a list
name[0] = "Ravindra"
print(name[0])
'''

'''
#program to find the largest number in a list
number = [11,23,13,44,15,26]
largetNumber = number[0]
for k in number:
    if largetNumber < k:
        largetNumber = k

print(largetNumber)

'''
#removing suplicate in a list
number = [11,23,11,15,13,44,15,26]
number.sort()
i=0
print(number)
for k in number:
    if k == number:
        largetNumber = k




