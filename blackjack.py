import random as r
def blackjack():
	global deck
	deck = [['A', '♠'],[2, '♠'],[3, '♠'], [4, '♠'],['5', '♠'],['6', '♠'],[7, '♠'],[8, '♠'],[9, '♠'],[10, '♠'],['J', '♠'],['Q', '♠'],['K', '♠'],['A', '♥'],[2, '♥'],[3, '♥'],[4, '♥'],[5, '♥'],[6, '♥'],[7, '♥'],[8, '♥'],[9, '♥'],[10, '♥'],['J', '♥'],['Q', '♥'],['K', '♥'],['A', '♦'],[2, '♦'],[3, '♦'],[4, '♦'],[5, '♦'],[6, '♦'],[7, '♦'],[8, '♦'],[9, '♦'],[10, '♦'],['J', '♦'],['Q', '♦'],['K', '♦'],['A', '♣'],[2, '♣'],[3, '♣'],[4, '♣'],[5, '♣'],[6, '♣'],[7, '♣'],[8, '♣'],[9, '♣'],[10, '♣'],['J', '♣'],['Q', '♣'],['K', '♣']]
	dealer = []
	player = []
	
	
	dealer.append(pickcard(deck))
	player.append(pickcard(deck))
	dealer.append(pickcard(deck))
	player.append(pickcard(deck))
	
	hand = ""
	pval = updateval(player,"p")
	hand = (updatehand(player))
	print("Your hand is: " + hand)
	print("The value of your hand is: " + str(pval))
	
	choice = (input("press 1 to hit, press 2 to pass:"))
	while choice != "1" and choice != "2":
		choice = (input("ERROR: press 1 to hit, press 2 to pass:"))
	
	
	if choice == "1":
		player.append(pickcard(deck))
		pval = updateval(player,"p")
		hand = (updatehand(player))
		print("Your hand is: " + hand)
		print("The value of your hand is: " + str(pval))
	
	if updateval(dealer,"d")<17:
		dealer.append(pickcard(deck))
	
	if len(dealer) == 2 and updateval(dealer,"p") == 21:
		print("The dealer has Black Jack! You lose.")
	elif len(player) == 2 and updateval(player,"p") == 21:
		print("You have Black Jack! You win.")
	elif updateval(player,"p") > 21:
		print("Your hand is above 21! You lose.")
	elif updateval(dealer,"p") > 21:
		print("The dealer's hand is above 21! You win.")
	elif updateval(player,"p") > updateval(dealer,"p"):
		print("Your hand is higher than the dealer's! You win!")
	else:
		print("You lose.")


def pickcard(deck):
	num = r.randrange(len(deck))
	card = deck[num]
	deck.pop(num)
	return card 



def updatehand(player):
	hand = ""
	for card in player:
		hand += str(card[0])
		hand += card[1]
		hand += ", "
	hand = hand[:-2]
	return(hand)

def updateval(player,v):
	value = 0
	aces = 0
	ten = False
	for card in player:
		if type(card[0]) == int:
			value += card[0]
			if card[0] == 10:
				ten = True
		elif type(card[0]) == "J" or type(card[0]) == "K" or type(card[0]) == "Q":
			value += 10
			ten = True
		else:
			aces += 1
	if v == "p":
		while aces > 0:
			if (value +(aces*11))>21:
				value += 1
			else:
				value += 11
			aces = aces-1
	if v == "d":
		while aces>0:
			if (value +(aces*11))>16:
				value += 1
			else:
				value += 11
			aces = aces-1
	return(value)

blackjack()









