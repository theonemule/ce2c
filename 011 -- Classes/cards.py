class card:
    
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    
    def show(self):
        return self.value + self.suit

Deck = []

for idx in range(0,52):
    cardValue = ""
    value = idx % 13    
    if (value == 0):
        cardValue = "A"
    elif (value == 12):
        cardValue = "K"
    elif (value == 11):
        cardValue = "Q"
    elif (value == 10):
        cardValue = "J"
    else:
        cardValue = str(value + 1)
    
    suit = idx // 13
    cardSuit = ""
    if(suit == 0):
        cardSuit = "♠"
    elif(suit == 1):
        cardSuit = "♥"
    elif(suit == 2):
        cardSuit = "♣"
    elif(suit == 3):
        cardSuit ="♦"
    
    Deck.append(card(cardValue, cardSuit))

for Card in Deck:
    print (Card.show())