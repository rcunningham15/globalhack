print(
"""
This is war. 
Rules are:

1. Deal out deck of 52 cards between two users.
2. Each player plays a card. Highest card wins; winner takes both cards.
3. If players tie, then each player puts down three cards, and the third
   card competes.
4. The war is over when one player is out of cards. The player with
   cards remaining is the winner.
   
"""
)

import random

deck = []
count1 = 0
count2 = 0
pdeck = []
cdeck = []

#create deck
while (count1 < 4):
    for x in range(2,15):
        deck.append(x)
    count1 = count1 + 1

#create player deck
while (count2 < 26):
    deal = random.choice(deck)
    deck.remove(deal)
    pdeck.append(deal)
    count2 = count2 + 1

print(pdeck)
print(len(pdeck))
print(deck)
print(len(deck))


def war():
    pwar1 = random.choice(pdeck)
    pwar2 = random.choice(pdeck)
    pwar3 = random.choice(pdeck)
    pwar4 = random.choice(pdeck)
    cwar1 = random.choice(deck)
    cwar2 = random.choice(deck)
    cwar3 = random.choice(deck)
    cwar4 = random.choice(deck)
   
    if(cwar4 > pwar4):
        print ("Their war!")
        deck.append(pwar1)
        deck.append(pwar2)
        deck.append(pwar3)
        deck.append(pwar4)
        #pdeck.remove(pwar1)
        #pdeck.remove(pwar2)
        #pdeck.remove(pwar3)
        #pdeck.remove(pwar4)
        print(len(pdeck))
        print(len(deck))
        
    elif(cwar4 < pwar4):
        print ("Your war!")
        pdeck.append(cwar1)
        pdeck.append(cwar2)
        pdeck.append(cwar3)
        pdeck.append(cwar4)
        #deck.remove(cwar1)
        #deck.remove(cwar2)
        #deck.remove(cwar3)
        #deck.remove(cwar4)
        print(len(pdeck))
        print(len(deck))
        
    elif(cwar4 == pwar4):
        print ("Another War!")
        war()
               
       
#gameplay
while(len(deck) > 0 or len(pdeck) > 0):
    pdraw = random.choice(pdeck)
    cdraw = random.choice(deck)
    print("Your draw: " + str(pdraw))
    print("Their draw: " + str(cdraw))
    
    if(cdraw > pdraw):
        print ("Their pair.")
        deck.append(pdraw)
        pdeck.remove(pdraw)
        print(len(pdeck))
        print(len(deck))
    
    elif(cdraw < pdraw):
        print ("Your pair.")
        pdeck.append(cdraw)
        deck.remove(cdraw)
        print(len(pdeck))
        print(len(deck))
    
    elif(cdraw == pdraw):
        print ("War!")
        war()
            
if (len(deck) == 0):
    print("You Win!")
if (len(pdeck) == 0):
    print("You Lose!")
            
        