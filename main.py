import random as r

Hearts = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
Diamonds = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
Clubs = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
Spades = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
deck = [Hearts, Clubs, Spades, Diamonds]
decksuits = ["Hearts", "Clubs", "Spades", "Diamonds"]
global runnum
runnum = 0


# Function to check for and handle duplicate cards
def get_unique_card(drawn_cards):
    while True:
        suit = r.choice(decksuits)
        suitnum = r.choice(deck)
        num = r.choice(suitnum)
        card = (num, suit)  # Create a tuple to represent the card
        if card not in drawn_cards:
            drawn_cards.add(card)  # Add the card to the set
            return num, suit, card


# Modified cardpick function
def cardpick():
    global drawn_cards  # Access the global set
    suit = r.choice(decksuits)
    suitnum = r.choice(deck)
    num = r.choice(suitnum)
    if x != 1:
        print(num, "of", suit)
        card = [num, suit]
    elif x == 1:
        print("(Card 2)")
    if num == "J" or num == "Q" or num == "K":
        value = 10
    elif num == "A":
        value = 11
    else:
        value = int(num)
    card = [num, suit]
    return value, num, suit, card


# Modified cardpickplayer function
def cardpickplayer():
    global drawn_cards
    num, suit, card = get_unique_card(drawn_cards)
    print(num, "of", suit)
    if num == "J" or num == "Q" or num == "K":
        value = 10
    elif num == "A":
        value = 1 if pval > 10 else 11
    else:
        value = int(num)
    return value


x = 0
dval = 0
drawn_cards = set()  # Initialize the set to track drawn cards

## dealer cards
print("------Dealers Cards------")
while x < 2:
    value, num, suit, card = cardpick()
    dval = dval + value
    x += 1
if dval == 21:
    print("Card 2:", num, "of", suit)
    print("Dealer has Blackjack, Player Loses")
    exit()
print(" ")
print("------Players Cards------")
pval = 0
x = 0
while x < 2:
    value = cardpickplayer()
    pval = pval + value
    x += 1
print("Hand Value:", pval)
print(" ")
if pval == 21:
    print("Player has Blackjack, Player Wins")
else:
    b = input("Hit or Stand?  ")
    b = b.lower()
    print("")
    while pval < 21:
        if b == "hit":
            pval = pval + cardpickplayer()
            print("Hand Value:", pval)
            if pval == 21:
                print("Player has Blackjack, Player Wins")
        elif b == "stand":
            if dval <= 16:
                print("------Dealers Hand (added cards) ------")
                print("Card 2:", num, "of", suit)
            while dval <= 16:
                value, num, suit, card = cardpick()
                dval = dval + value
            if dval > pval and dval <= 21:
                print("Dealer Hand Value:", dval)
                print("Player Hand Value:", pval)
                print(" ")
                print("Dealer Wins")
                break
            if dval < pval and pval <= 21:
                print("Dealer Hand Value:", dval)
                print("Player Hand Value:", pval)
                print(" ")
                print("Player Wins")
                break
            if dval == pval:
                print("Dealer Hand Value:", dval)
                print("Player Hand Value:", pval)
                print(" ")
                print("No Winner")
                break
        if pval < 21 and b != "stand":
            b = input("Hit or Stand?  ")
            b = b.lower()
            print("")
        elif pval > 21:
            print("Player Busts, Dealer Wins")
            break
