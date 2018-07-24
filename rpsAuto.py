import random 
p1 = random.choice(["rock","paper","scissors"])
p2 = random.choice(["rock","paper","scissors"])
print("Player1: " + p1)
print("Player2: " + p2)
if p1 == "rock":
    if p2 == "paper":
        print("Player2 wins!")
    elif p2 == "scissors":
        print("Player1 wins!")
    elif p2 == "rock":
        print("It's a tie!")
elif p1 == "paper":
    if p2 == "scissors":
        print("Player2 wins!")
    elif p2 == "rock":
        print("Player1 wins!")
    elif p2 == "paper":
        print("It's a tie!")
elif p1 == "scissors":
    if p2 == "rock":
        print("Player2 wins!")
    elif p2 == "paper":
        print("Player1 wins!")
    elif p2 == "scissors":
        print("It's a tie!")
    