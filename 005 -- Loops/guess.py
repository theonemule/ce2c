import random

print(" * * * GUESS THAT NUMBER * * *")
print()
maximum = int(input("What is the maximum you would like to try?" ))
maxAttempts = int(input("How many attemtps would you like? "))

number = random.randint(1,maximum)

attemptCount = 0
guess = -1

while guess != number and attemptCount < maxAttempts:
    guess = int(input("Guess a number: "))
    
    if guess > number:
        print("Too high!")
    elif guess < number:
        print("Too low!")
        
    attemptCount = attemptCount + 1
        
if guess == number:
    print("You got it!")
else:    
    print("Better luck next time. The number was " + str(number))