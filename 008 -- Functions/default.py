def add(val1 = 3, val2 = 4):
    return val1 + val2

def getNumber(varName = ""):
    val = ""
    while not str.isnumeric(val):
        if varName == "":
            val = input("Enter a numeric value: ")    
        else:
            val = input("Enter a numeric value for " + varName + ": ")    
    return float(val)

print(add())
print(add(1))
print(add(val2 = 1))
print(add(val2 = 1,val1 = 9))

print(getNumber())