import random
import poker

def deal(numhands, numcards=5):
	deck = [r+s for r in '23456789TJQKA' for s in 'SCDH']
	random.shuffle(deck)
	return [deck[numcards*i:numcards*(i+1)] for i in range(numhands)]

hands = deal(3)
print("Different sets of cards")
print(hands)
print("Winning card set")
print(poker.play(hands))