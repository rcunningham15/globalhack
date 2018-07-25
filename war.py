done = False
import random
#while (done == False):
print ("This is War.")


deck = ["Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace"]
pdeck = 26;
cdeck = 26;


while (pdeck > 0 or cdeck > 0):
    p1 = random.choice(deck)
    c1 = random.choice(deck)
    
    flip = raw_input("Flip: y/n? ")
    if (flip == "y"):
        print (p1)
        print (c1)
        
        if (p1 == c1):
            flip2 = raw_input("Flip: y/n? ")
            if(flip2 == "y"):
                flip3 = raw_input("Flip: y/n? ")
                if(flip3 == "y"):
                    flip4 = raw_input("Flip: y/n? ")
                    if(flip4 == "y"): 
                        p1 = random.choice(deck)
                        c1 = random.choice(deck)
                        print(p1)
                        print(c1)
                        
                        if (p1 == "Two"):
                            pdeck = pdeck - 4
                            cdeck = cdeck + 4 
                            print("Player2's war!")
                    
                    
                        elif (p1 == "Three"):
                            if (c1 == "Two"):
                                pdeck = pdeck + 4
                                cdeck = cdeck - 4
                                print("Your war!")
                        else:    
                            pdeck = pdeck - 4
                            cdeck = cdeck + 4
                            print("Player2's war!")
                        
                        
                        if (p1 == "Four"):
                            if (c1 == "Three" or c1 == "Two"):
                                pdeck = pdeck + 4
                                cdeck = cdeck - 4
                                print("Your war!")
                        else:    
                            pdeck = pdeck - 4
                            cdeck = cdeck + 4
                            print("Player2's war!")
                            
                            
                        if (p1 == "Five"):
                            if (c1 == "Four" or c1 == "Three" or c1 == "Two"):
                                pdeck = pdeck + 4
                                cdeck = cdeck - 4
                                print("Your war!")
                            else:    
                                pdeck = pdeck - 4
                                cdeck = cdeck + 4
                                print("Player2's war!")
                                
                                
                        if (p1 == "Six"):
                            if (c1 == "Five" or c1 == "Four" or c1 == "Three" or c1 == "Two"):
                                pdeck = pdeck + 4
                                cdeck = cdeck - 4
                                print("Your war!")
                            else:    
                                pdeck = pdeck - 4
                                cdeck = cdeck + 4
                                print("Player2's war!")
                        
                        if (p1 == "Seven"):
                            if (c1 == "Six" or c1 == "Five" or c1 == "Four" or c1 == "Three" or c1 == "Two"):
                                pdeck = pdeck + 4
                                cdeck = cdeck - 4
                                print("Your war!")
                            else:    
                                pdeck = pdeck - 4
                                cdeck = cdeck + 4
                                print("Player2's war!")
                                
                        if (p1 == "Eight"):
                            if (c1 == "Seven" or c1 == "Six" or c1 == "Five" or c1 == "Four" or c1 == "Three" or c1 == "Two"):
                                pdeck = pdeck + 4
                                cdeck = cdeck - 4
                                print("Your war!")
                            else:    
                                pdeck = pdeck - 4
                                cdeck = cdeck + 4
                                print("Player2's war!")
                        
                        if (p1 == "Nine"):
                            if (c1 == "Eight" or c1 == "Seven" or c1 == "Six" or c1 == "Five" or c1 == "Four" or c1 == "Three" or c1 == "Two"):
                                pdeck = pdeck + 4
                                cdeck = cdeck - 4
                                print("Your war!")
                            else:    
                                pdeck = pdeck - 4
                                cdeck = cdeck + 4
                                print("Player2's war!")
                        
                        if (p1 == "Ten"):
                            if (c1 == "Nine" or c1 == "Eight" or c1 == "Seven" or c1 == "Six" or c1 == "Five" or c1 == "Four" or c1 == "Three" or c1 == "Two"):
                                pdeck = pdeck + 4
                                cdeck = cdeck - 4
                                print("Your war!")
                            else:    
                                pdeck = pdeck - 4
                                cdeck = cdeck + 4
                                print("Player2's war!")
                        
                        if (p1 == "Jack"):
                            if (c1 == "Ten" or c1 == "Nine" or c1 == "Eight" or c1 == "Seven" or c1 == "Six" or c1 == "Five" or c1 == "Four" or c1 == "Three" or c1 == "Two"):
                                pdeck = pdeck + 4
                                cdeck = cdeck - 4
                                print("Your war!")
                            else:    
                                pdeck = pdeck - 4
                                cdeck = cdeck + 4
                                print("Player2's war!")
                                
                        if (p1 == "Queen"):
                            if (c1 == "Jack" or c1 == "Ten" or c1 == "Nine" or c1 == "Eight" or c1 == "Seven" or c1 == "Six" or c1 == "Five" or c1 == "Four" or c1 == "Three" or c1 == "Two"):
                                pdeck = pdeck + 4
                                cdeck = cdeck - 4
                                print("Your war!")
                            else:    
                                pdeck = pdeck - 4
                                cdeck = cdeck + 4
                                print("Player2's war!")
                        
                        if (p1 == "King"):
                            if (c1 == "Queen" or c1 == "Jack" or c1 == "Ten" or c1 == "Nine" or c1 == "Eight" or c1 == "Seven" or c1 == "Six" or c1 == "Five" or c1 == "Four" or c1 == "Three" or c1 == "Two"):
                                pdeck = pdeck + 4
                                cdeck = cdeck - 4
                                print("Your war!")
                            else:    
                                pdeck = pdeck - 4
                                cdeck = cdeck + 4
                                print("Player2's war!")
                        
                        if (p1 == "Ace"):
                            pdeck = pdeck - 4
                            cdeck = cdeck + 4
                            print("Your war!")
#NEWNEWNEWNEWNEWNEW           
#NEWNEWNEWNEWNEWNEW
#NEWNEWNEWNEWNEWNEW           
#NEWNEWNEWNEWNEWNEW
#NEWNEWNEWNEWNEWNEW           
#NEWNEWNEWNEWNEWNEW
        else:
            if (p1 == "Two"):
                pdeck = pdeck - 1
                cdeck = cdeck + 1 
                print("Player2's pair!")
        
        
            if (p1 == "Three"):
                if (c1 == "Two"):
                        pdeck = pdeck + 1
                        cdeck = cdeck - 1
                        print("Your pair!")
                else:    
                    pdeck = pdeck - 1
                    cdeck = cdeck + 1
                    print("Player2's pair!")
                
                
                if (p1 == "Four"):
                    if (c1 == "Three" or c1 == "Two"):
                        pdeck = pdeck + 1
                        cdeck = cdeck - 1
                        print("Your pair!")
                else:    
                    pdeck = pdeck - 1
                    cdeck = cdeck + 1
                    print("Player2's pair!")
                    
                    
                if (p1 == "Five"):
                    if (c1 == "Four" or c1 == "Three" or c1 == "Two"):
                        pdeck = pdeck + 1
                        cdeck = cdeck - 1
                        print("Your pair!")
                    else:    
                        pdeck = pdeck - 1
                        cdeck = cdeck + 1
                        print("Player2's pair!")
                        
                        
                if (p1 == "Six"):
                    if (c1 == "Five" or c1 == "Four" or c1 == "Three" or c1 == "Two"):
                        pdeck = pdeck + 1
                        cdeck = cdeck - 1
                        print("Your pair!")
                    else:    
                        pdeck = pdeck - 1
                        cdeck = cdeck + 1
                        print("Player2's pair!")
                
                if (p1 == "Seven"):
                    if (c1 == "Six" or c1 == "Five" or c1 == "Four" or c1 == "Three" or c1 == "Two"):
                        pdeck = pdeck + 1
                        cdeck = cdeck - 1
                        print("Your pair!")
                    else:    
                        pdeck = pdeck - 1
                        cdeck = cdeck + 1
                        print("Player2's pair!")
                        
                if (p1 == "Eight"):
                    if (c1 == "Seven" or c1 == "Six" or c1 == "Five" or c1 == "Four" or c1 == "Three" or c1 == "Two"):
                        pdeck = pdeck + 1
                        cdeck = cdeck - 1
                        print("Your pair!")
                    else:    
                        pdeck = pdeck - 1
                        cdeck = cdeck + 1
                        print("Player2's pair!")
                
                if (p1 == "Nine"):
                    if (c1 == "Eight" or c1 == "Seven" or c1 == "Six" or c1 == "Five" or c1 == "Four" or c1 == "Three" or c1 == "Two"):
                        pdeck = pdeck + 1
                        cdeck = cdeck - 1
                        print("Your pair!")
                    else:    
                        pdeck = pdeck - 1
                        cdeck = cdeck + 1
                        print("Player2's pair!")
                
                if (p1 == "Ten"):
                    if (c1 == "Nine" or c1 == "Eight" or c1 == "Seven" or c1 == "Six" or c1 == "Five" or c1 == "Four" or c1 == "Three" or c1 == "Two"):
                        pdeck = pdeck + 1
                        cdeck = cdeck - 1
                        print("Your pair!")
                    else:    
                        pdeck = pdeck - 1
                        cdeck = cdeck + 1
                        print("Player2's pair!")
                
                if (p1 == "Jack"):
                    if (c1 == "Ten" or c1 == "Nine" or c1 == "Eight" or c1 == "Seven" or c1 == "Six" or c1 == "Five" or c1 == "Four" or c1 == "Three" or c1 == "Two"):
                        pdeck = pdeck + 1
                        cdeck = cdeck - 1
                        print("Your pair!")
                    else:    
                        pdeck = pdeck - 1
                        cdeck = cdeck + 1
                        print("Player2's pair!")
                        
                if (p1 == "Queen"):
                    if (c1 == "Jack" or c1 == "Ten" or c1 == "Nine" or c1 == "Eight" or c1 == "Seven" or c1 == "Six" or c1 == "Five" or c1 == "Four" or c1 == "Three" or c1 == "Two"):
                        pdeck = pdeck + 1
                        cdeck = cdeck - 1
                        print("Your pair!")
                    else:    
                        pdeck = pdeck - 1
                        cdeck = cdeck + 1
                        print("Player2's pair!")
                
                if (p1 == "King"):
                    if (c1 == "Queen" or c1 == "Jack" or c1 == "Ten" or c1 == "Nine" or c1 == "Eight" or c1 == "Seven" or c1 == "Six" or c1 == "Five" or c1 == "Four" or c1 == "Three" or c1 == "Two"):
                        pdeck = pdeck + 1
                        cdeck = cdeck - 1
                        print("Your pair.")
                    else:    
                        pdeck = pdeck - 1
                        cdeck = cdeck + 1
                        print("Player2's pair!")
                
                if (p1 == "Ace"):
                    pdeck = pdeck - 1
                    cdeck = cdeck + 1
                    print("Your pair!")
    
    if(pdeck == 0):
        print("You lose.")
    if(cdeck == 0):
        print("You win.")
            
        
        
        