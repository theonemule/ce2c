AlphabetTuple = ("A","B","C","D","E","F")
AlphabetList = ["A","B","C","D","E","F"]

Letter = input("Give me a letter: ")

if Letter in AlphabetList:
    print(Letter + " is in AlphabetList.")
    print ("The index of the letter in AlphabetList is " + str(AlphabetList.index(Letter)))
else:
    print(Letter + " is NOT in AlphabetList.")
    
    
    
