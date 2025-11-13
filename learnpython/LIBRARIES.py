#RANDOM MODULE
'''import random
coin=random.choice(["Heads", "Tails"])
print(f"The coin landed on {coin}.")'''

#RANDOM MODULE @ 2
#USED TO IMPORT SPECIFIC FUNCTIONS FROM A MODULE
'''from random import choice
coin=choice(["Heads","Tails"])
print(f"The coin flipped on the side of {coin}")'''

#RANDOM MODULE @ 3
#USED TO GENERATE A RANDOM NUMBER BETWEEN TWO VALUES
'''import random
number=random.randint(1, 10)
print(number)'''

#RANDOM MODULE @ 4
#USED TO SHUFFLE THE SEQUENCE ORDERS
'''import random
cards=["Ace","King","Queen","Jack","10","9","8","7","6","5","4","3","2"]
random.shuffle(cards)
for card in cards:
    print(card,end=" ")'''
