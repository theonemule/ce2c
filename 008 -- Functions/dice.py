import random

def rollDice(numberOfDice, sides):
    for roll in range(0, numberOfDice):
        print(random.randint(1, sides))

def getNumber(varName = ""):
    val = ""
    while not str.isnumeric(val):
        if varName == "":
            val = input("Enter a numeric value: ")    
        else:
            val = input("Enter a numeric value for " + varName + ": ")    
        
        if str.isnumeric(val) and int(val) < 1:
            val = ""
            
    return int(val)

diceCount = getNumber("dice count")
diceSides = getNumber("sides")

rollDice(diceCount, diceSides)