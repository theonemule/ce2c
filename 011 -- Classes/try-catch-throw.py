
def addPositiveNumbers(a,b):
    if a < 0 or b < 0:
        raise Exception("Numbers must be positive")
    return a + b

try:
    print(addPositiveNumbers(2,3))
except Exception as err:
    print(err)
else:
    print("Everything is good!")
    

try:
    print(addPositiveNumbers(-2,3))
except Exception as err:
    print(err)
else:
    print("Everything is good!")