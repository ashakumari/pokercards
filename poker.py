def play(hands):
	"Return the best hand: poker[hand,...]) => hand"
	return allmax(hands, key=hand_rank)

def allmax(iterable, key=None):
	result, maxval = [], None
	key = key or (lambda x: x)
	for x in iterable:
		xval = key(x)
		if not result or xval > maxval:
			result, maxval = [x], xval
		elif xval == maxval:
			result.append(x)
	return result

def card_ranks(cards):
	"Return the list of the ranks, sorted with highest first"
	ranks = ['--23456789TJQKA'.index(r) for r,s in cards]
	ranks.sort(reverse=True)
	if ranks == [14, 5, 4, 3, 2]:
		return [5, 4, 3, 2, 1]
	return ranks

def hand_rank(hand):
	"Return a value indicating the ranking of a hand"
	ranks = card_ranks(hand)
	if straight(ranks) and flush(hand):
		return (8, max(ranks))
	elif kind(4, ranks):
		return (7, kind(4, ranks), kind(1, ranks))
	elif kind(3, ranks) and kind(2, ranks):
		return (6, kind(3, ranks), kind(2, ranks))
	elif flush(hand):
		return (5, ranks)
	elif straight(ranks):
		return (4, max(ranks))
	elif kind(3, ranks):
		return (3, kind(3, ranks), ranks)
	elif two_pairs(ranks):
		return (2, two_pairs(ranks), ranks)
	elif kind(2, ranks):
		return (1, kind(2, ranks), ranks)
	else:
		return (0, ranks)

def kind(n, ranks):
	for r in ranks:
		if ranks.count(r) == n:
			return r
	return None


def straight(ranks):
	"Return True if the ordered ranks form a 5-card straight"
	return (max(ranks)-min(ranks) == 4 and len(set(ranks))) == 5


def flush(cards):
	"Retrun True if all the cards have the same suit"
	suits = [s for r,s in cards]
	return len(set(suits)) == 1

def two_pairs(ranks):
	pair = kind(2, ranks)
	lowpair = kind(2, list(reversed(ranks)))
	if pair and pair != lowpair:
		return (pair, lowpair)
	return None

def test():
	"Test cases for the functions in poker program"
	sf = "6C 7C 8C 9C TC".split() # straight flush
	fk = "9D 9H 9S 9C 7D".split() # four kind
	fh = "TD TC TH 7C 7D".split() # full house
	tp = "5S 5D 9C 9S 6H".split() # two pair
	s1 = "AS 2S 3S 4S 5C".split() # A-5 straight
	s2 = "2C 3C 4C 5S 6S".split() # 2-6 straight
	ah = "AS 2S 3S 4S 6C".split() # A highest
	sh = "2S 3S 4S 6C 7D".split() # 7 highest
	sfranks = card_ranks(sf)
	fkranks = card_ranks(fk)
	fhranks = card_ranks(fh)
	tpranks = card_ranks(tp)
	assert sfranks == [10, 9, 8, 7, 6]
	assert fkranks == [9, 9, 9, 9, 7]
	assert fhranks == [10, 10, 10, 7, 7]
	assert straight(sfranks) == True
	assert straight(fkranks) == False
	assert flush(sf) == True
	assert flush(fk) == False
	assert kind(4, fkranks) == 9
	assert kind(3, fkranks) == None
	assert kind(2, fkranks) == None
	assert kind(1, fkranks) == 7
	assert two_pairs(fkranks) == None
	assert two_pairs(tpranks) == (9, 5)
	assert hand_rank(sf) == (8, 10)
	assert hand_rank(fk) == (7, 9, 7)
	assert hand_rank(fh) == (6, 10, 7)
	assert hand_rank(s1) == (4, 5)
	assert hand_rank(s2) == (4, 6)
	assert poker([sf, fk, fh]) == [sf]
	assert poker([fk, fh]) == [fk]
	assert poker([fh, fh]) == [fh, fh]
	assert poker([sf]) == [sf]
	assert poker([sf] + 99*[fh]) == [sf]
	assert poker([s1, s2, ah, sh]) == [s2]
	return "tests pass"
