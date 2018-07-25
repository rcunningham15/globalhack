"""
Implement the card game war. Rules are:

1. Deal out deck of 52 cards between two users.
2. Each player plays a card. Higher card wins. Winner takes both cards.
3. If players tie, then each player puts down three cards, and the third
   card competes.
   If a player has less than 3 cards, then they put down all of their cards
   and their final card competes against the other player's third card.
   Continue doing this until tie is broken.
   Winner takes all cards.
4. Game is over when a player doesn't have any cards. The player with
   cards remaining is the winner.
"""
import random

def generate_deck(suites=4, type_cards=13):
    "Generate a randomized deck of cards."
    cards = []
    for suite in range(suites):
        for type_card in range(1, type_cards+1):
            cards.append(type_card)
    random.shuffle(cards)
    return cards

def play_war(deck):
    a_cards = deck[:len(deck)/2]
    b_cards = deck[len(deck)/2:]
    a_stash = []
    b_stash = []

    round = 1
    while a_cards and b_cards:
        # by using pop, we're playing from the end forward
        a_card = a_cards.pop()
        b_card = b_cards.pop()

        if a_card == b_card:
            a_stash.extend([a_card]+a_cards[-3:])
            a_cards = a_cards[:-3]
            a_cards.append(a_stash.pop())

            b_stash.extend([b_card]+b_cards[-3:])
            b_cards = b_cards[:-3]
            b_cards.append(b_stash.pop())
        elif a_card > b_card:
            # ordering of a_stash and b_stash is undefined by game rules
            a_cards = [a_card, b_card] + a_stash + b_stash + a_cards
            a_stash = []
            b_stash = []
        elif b_card > a_card:
            # ordering of a_stash and b_stash is undefined by game rules
            b_cards = [b_card, a_card] + b_stash + a_stash + b_cards
            a_stash = []
            b_stash = []

        print "round %s: a_cards: %s, a_stash %s, b_cards %s, b_stash %s" %(round, len(a_cards), len(a_stash), len(b_cards), len(b_stash))
        round += 1


if __name__ == "__main__":
    deck = generate_deck()
    play_war(deck)