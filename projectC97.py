#Setup
import random


#Display
for i in range(1, 3):
    print("\n")

diff = int(input("Enter a difficulty level from 5 to 10: "))
numToGuess = random.randint(1, diff)

for trys in range(1, 6):
    ans = int(input("My Guess: "))
    if trys<=5:
        if ans == numToGuess:
            print("Nice you got it right!")
            break
        else:
            print("Wrong answer! You have ", 5-trys, " tries left!", sep="")
            continue
    else:
        print("Opps! You ran out of trys, the number was ", numToGuess, sep="")


for i in range(1, 3):
    print("\n")