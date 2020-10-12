import random

Deck = []

for idx in range(0,52):
    card = ""
    value = idx % 13    
    if (value == 0):
        card = "A"
    elif (value == 12):
        card = "K"
    elif (value == 11):
        card = "Q"
    elif (value == 10):
        card = "J"
    else:
        card = str(value + 1)
    
    suit = idx // 13
    if(suit == 0):
        card += "♠"
    elif(suit == 1):
        card += "♥"
    elif(suit == 2):
        card += "♣"
    elif(suit == 3):
        card += "♦"
    
    Deck.append(card)

print ('\nDeck before Shuffling\n')
print(Deck)

for idx in range(0,52):
    randomIdx = random.randint(0,51)
    removedCard = Deck[randomIdx]
    Deck[randomIdx] = Deck[idx]
    Deck[idx] = removedCard
    
print ('\nDeck after Shuffling\n')
print(Deck)    

draw = ""
while(len(Deck) > 0 and draw != "Q"):
    randomIdx = random.randint(0,len(Deck) - 1)
    drawnCard = Deck[randomIdx]
    del Deck[randomIdx]
    print("\n Card Drawn: " + drawnCard)
    draw = input("\n Press ENTER to draw again or enter Q to quit: ")