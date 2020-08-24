print()
print(" * * * The Drake Equation * * *")
print()

R = int(input("How many new stars form in our galaxy per year? "))
P = float(input("Fraction of stars with planet (0-1)? "))
E = int(input("Planets per star that can support life ? "))
L = float(input("Fraction of planets were life develops? (0-1)? "))
I = float(input("Fraction of planets with intelligent life? (0-1)? "))
C = float(input("Fraction of planets that develop detectable signals? (0-1)? "))
T = int(input("How many years would civilization release these signals? "))

D = R * P * E * L * I * C * T

print()
print()
print("Number of civilizations that might be possible: " + str(D))

