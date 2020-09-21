myWords = {
        "zorse": "A hybrid horse and zebra",
        "mule": "A hybrid horse and donkey",
        "zonkey": "A hybrid zebra and donkey",
    }

print(myWords)

#Change a value
myWords["zonkey"] = "A hybrid donkey and zebra"

print(myWords)

#Add a value
myWords["Prius"] = "A hybrid electric and gas vehicle"

print(myWords)

#Remove a value
del myWords["mule"]

print(myWords)