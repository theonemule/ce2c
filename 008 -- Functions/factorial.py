def factorial(val = 1):
    if val == 1:
        return 1
    else:
        return val + factorial(val - 1)
    
print(factorial(3)) # 6