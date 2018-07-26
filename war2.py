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

#print(pdeck)
#print(len(pdeck))
#print(deck)
#print(len(deck))

def athirdwar():
    pwar1 = random.choice(pdeck)
    pwar2 = random.choice(pdeck)
    pwar3 = random.choice(pdeck)
    pwar4 = random.choice(pdeck)
    cwar1 = random.choice(deck)
    cwar2 = random.choice(deck)
    cwar3 = random.choice(deck)
    cwar4 = random.choice(deck)
    pwar5 = random.choice(pdeck)
    pwar6 = random.choice(pdeck)
    pwar7 = random.choice(pdeck)
    pwar8 = random.choice(pdeck)
    cwar5 = random.choice(deck)
    cwar6 = random.choice(deck)
    cwar7 = random.choice(deck)
    cwar8 = random.choice(deck)
    pwar9 = random.choice(pdeck)
    pwar10 = random.choice(pdeck)
    pwar11 = random.choice(pdeck)
    pwar12 = random.choice(pdeck)
    cwar9 = random.choice(deck)
    cwar10 = random.choice(deck)
    cwar11 = random.choice(deck)
    cwar12 = random.choice(deck)
    
    flip = raw_input("Flip 1: y/n? ")
    if (flip == "y"): 
       flip = raw_input("Flip 2: y/n? ")
       if (flip == "y"):
           flip = raw_input("Flip 3: y/n? ")
           if (flip == "y"):
               
                if(cwar8 > pwar8):
                    print ("Their war!")
                    deck.append(pwar5)
                    deck.append(pwar6)
                    deck.append(pwar7)
                    deck.append(pwar8)
                    pdeck.remove(pwar5)
                    pdeck.remove(pwar6)
                    pdeck.remove(pwar7)
                    pdeck.remove(pwar8)
                    deck.append(pwar1)
                    deck.append(pwar2)
                    deck.append(pwar3)
                    deck.append(pwar4)
                    pdeck.remove(pwar1)
                    pdeck.remove(pwar2)
                    pdeck.remove(pwar3)
                    pdeck.remove(pwar4)
                    deck.append(pwar9)
                    deck.append(pwar10)
                    deck.append(pwar11)
                    deck.append(pwar12)
                    pdeck.remove(pwar9)
                    pdeck.remove(pwar10)
                    pdeck.remove(pwar11)
                    pdeck.remove(pwar12)
                    
                    print(len(pdeck))
                    print(len(deck))
                    
                elif(cwar8 < pwar8):
                    print ("Your war!")
                    pdeck.append(cwar5)
                    pdeck.append(cwar6)
                    pdeck.append(cwar7)
                    pdeck.append(cwar8)
                    deck.remove(cwar5)
                    deck.remove(cwar6)
                    deck.remove(cwar7)
                    deck.remove(cwar8)
                    pdeck.append(cwar1)
                    pdeck.append(cwar2)
                    pdeck.append(cwar3)
                    pdeck.append(cwar4)
                    deck.remove(cwar1)
                    deck.remove(cwar2)
                    deck.remove(cwar3)
                    deck.remove(cwar4)
                    pdeck.append(cwar9)
                    pdeck.append(cwar10)
                    pdeck.append(cwar11)
                    pdeck.append(cwar12)
                    deck.remove(cwar9)
                    deck.remove(cwar10)
                    deck.remove(cwar11)
                    deck.remove(cwar12)
                    print(len(pdeck))
                    print(len(deck))
                    
                elif(cwar8 == pwar8):
                    print ("Another War!")
                    war()
   
def anotherwar():
    pwar1 = random.choice(pdeck)
    pwar2 = random.choice(pdeck)
    pwar3 = random.choice(pdeck)
    pwar4 = random.choice(pdeck)
    cwar1 = random.choice(deck)
    cwar2 = random.choice(deck)
    cwar3 = random.choice(deck)
    cwar4 = random.choice(deck)
    pwar5 = random.choice(pdeck)
    pwar6 = random.choice(pdeck)
    pwar7 = random.choice(pdeck)
    pwar8 = random.choice(pdeck)
    cwar5 = random.choice(deck)
    cwar6 = random.choice(deck)
    cwar7 = random.choice(deck)
    cwar8 = random.choice(deck)
    flip = raw_input("Flip 1: y/n? ")
    if (flip == "y"): 
       flip = raw_input("Flip 2: y/n? ")
       if (flip == "y"):
           flip = raw_input("Flip 3: y/n? ")
           if (flip == "y"):
               
                if(cwar8 > pwar8):
                    print ("Their war!")
                    deck.append(pwar5)
                    deck.append(pwar6)
                    deck.append(pwar7)
                    deck.append(pwar8)
                    pdeck.remove(pwar5)
                    pdeck.remove(pwar6)
                    pdeck.remove(pwar7)
                    pdeck.remove(pwar8)
                    deck.append(pwar1)
                    deck.append(pwar2)
                    deck.append(pwar3)
                    deck.append(pwar4)
                    pdeck.remove(pwar1)
                    pdeck.remove(pwar2)
                    pdeck.remove(pwar3)
                    pdeck.remove(pwar4)
                    print(len(pdeck))
                    print(len(deck))
                    
                elif(cwar8 < pwar8):
                    print ("Your war!")
                    pdeck.append(cwar5)
                    pdeck.append(cwar6)
                    pdeck.append(cwar7)
                    pdeck.append(cwar8)
                    deck.remove(cwar5)
                    deck.remove(cwar6)
                    deck.remove(cwar7)
                    deck.remove(cwar8)
                    pdeck.append(cwar1)
                    pdeck.append(cwar2)
                    pdeck.append(cwar3)
                    pdeck.append(cwar4)
                    deck.remove(cwar1)
                    deck.remove(cwar2)
                    deck.remove(cwar3)
                    deck.remove(cwar4)
                    print(len(pdeck))
                    print(len(deck))
                    
                elif(cwar8 == pwar8):
                    print ("Another War!")
                    athirdwar()
    
def war():
    pwar1 = random.choice(pdeck)
    pwar2 = random.choice(pdeck)
    pwar3 = random.choice(pdeck)
    pwar4 = random.choice(pdeck)
    cwar1 = random.choice(deck)
    cwar2 = random.choice(deck)
    cwar3 = random.choice(deck)
    cwar4 = random.choice(deck)
    flip = raw_input("Flip 1: y/n? ")
    if (flip == "y"): 
       flip = raw_input("Flip 2: y/n? ")
       if (flip == "y"):
           flip = raw_input("Flip 3: y/n? ")
           if (flip == "y"):
               
                if(cwar4 > pwar4):
                    print ("Their war!")
                    deck.append(pwar1)
                    deck.append(pwar2)
                    deck.append(pwar3)
                    deck.append(pwar4)
                    pdeck.remove(pwar1)
                    pdeck.remove(pwar2)
                    pdeck.remove(pwar3)
                    pdeck.remove(pwar4)
                    print("You have " + str(len(pdeck)) + " cards.")
                    print("They have " + str(len(deck)) + " cards.")
                    
                elif(cwar4 < pwar4):
                    print ("Your war!")
                    pdeck.append(cwar1)
                    pdeck.append(cwar2)
                    pdeck.append(cwar3)
                    pdeck.append(cwar4)
                    deck.remove(cwar1)
                    deck.remove(cwar2)
                    deck.remove(cwar3)
                    deck.remove(cwar4)
                    print("You have " + str(len(pdeck)) + " cards.")
                    print("They have " + str(len(deck)) + " cards.")
                    
                elif(cwar4 == pwar4):
                    print ("Another War!")
                    anotherwar()
       
def cardnamenowar():
    if (pdraw == 2):
        pname = "Two"
    elif (pdraw == 3):
        pname = "Three"
    elif (pdraw == 4):
        pname = "Four"
    elif (pdraw == 5):
        pname = "Five"
    elif (pdraw == 6):
        pname = "Six"
    elif (pdraw == 7):
        pname = "Seven"
    elif (pdraw == 8):
        pname = "Eight"
    elif (pdraw == 9):
        pname = "Nine"
    elif (pdraw == 10):
        pname = "Ten"
    elif (pdraw == 11):
        pname = "Jack"
    elif (pdraw == 12):
        pname = "Queen"
    elif (pdraw == 13):
        pname = "King"
    elif (pdraw == 14):
        pname = "Ace"
    
    elif (cdraw == 2):
        cname = "Two"
    elif (cdraw == 3):
        cname = "Three"
    elif (cdraw == 4):
        cname = "Four"
    elif (cdraw == 5):
        cname = "Five"
    elif (cdraw == 6):
        cname = "Six"
    elif (cdraw == 7):
        cname = "Seven"
    elif (cdraw == 8):
        cname = "Eight"
    elif (cdraw == 9):
        cname = "Nine"
    elif (cdraw == 10):
        cname = "Ten"
    elif (cdraw == 11):
        cname = "Jack"
    elif (cdraw == 12):
        cname = "Queen"
    elif (cdraw == 13):
        cname = "King"
    elif (cdraw == 14):
        cname = "Ace"    
               
#gameplay
while(len(deck) > 0 or len(pdeck) > 0):
    flip = raw_input("Flip: y/n? ")
    if (flip == "y"):
        pdraw = random.choice(pdeck)
        cdraw = random.choice(deck)
        cardnamenowar()
        print("Your draw: " + pname)
        print("Their draw: " + cname)
        
        if(cdraw > pdraw):
            print ("""
            Their pair.
            """)
            deck.append(pdraw)
            pdeck.remove(pdraw)
            print("You have " + str(len(pdeck)) + " cards.")
            print("They have " + str(len(deck)) + " cards.")
        
        elif(cdraw < pdraw):
            print ("""
            Your pair.
            """)
            pdeck.append(cdraw)
            deck.remove(cdraw)
            print("You have " + str(len(pdeck)) + " cards.")
            print("They have " + str(len(deck)) + " cards.")
        
        elif(cdraw == pdraw):
            print ("War!")
            war()
            
if (len(deck) == 0):
    print("You Win!")
if (len(pdeck) == 0):
    print("You Lose!")
            
        