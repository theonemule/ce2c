def add(val1, val2):
    return val1 + val2

def getNumber(varName):
    val = ""
    while not str.isnumeric(val):
        val = input("Enter a numeric value for " + varName + ": ")
    
    return float(val)        
        
print(add(2,3))

mynum1 = getNumber("mynum1")
mynum2 = getNumber("mynum2")

print(add(mynum1, mynum2))