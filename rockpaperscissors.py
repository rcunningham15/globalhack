import random 
p1 = raw_input("Player1: ")
p2 = random.choice(["rock","paper","scissors"])
if p1 == "rock":
    print("Player2: " + p2)
    if p2 == "paper":
        print("You lose :(")
    elif p2 == "scissors":
        print("You win!")
    elif p2 == "rock":
        print("It's a tie!")
elif p1 == "paper":
    print("Player2: " + p2)
    if p2 == "scissors":
        print("You lose :(")
    elif p2 == "rock":
        print("You win!")
    elif p2 == "paper":
        print("It's a tie!")
elif p1 == "scissors":
    print("Player2: " + p2)
    if p2 == "rock":
        print("You lose :(")
    elif p2 == "paper":
        print("You win!")
    elif p2 == "scissors":
        print("It's a tie!")
elif p1 != "rock" and p1 != "paper" and p1 != "scissors":
    print("Oops! Please choose rock, paper, or scissors.")
    