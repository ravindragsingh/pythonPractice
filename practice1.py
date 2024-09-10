
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
