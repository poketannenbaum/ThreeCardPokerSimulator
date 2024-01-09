import random
from collections import Counter
class deck_init:
	def __init__(self, id, rank, suit, value):
		self.id = id
		self.rank = rank
		self.suit = suit
		self.value = value
deck = []

deck.append(deck_init(53, "Joker", 'NA', 69))
deck.append(deck_init(52, "A", '♤', 14))
deck.append(deck_init(51, "K", '♤', 13))
deck.append(deck_init(50, "Q", '♤', 12))
deck.append(deck_init(49, "J", '♤', 11))
deck.append(deck_init(48, "10", '♤', 10))
deck.append(deck_init(47, "9", '♤', 9))
deck.append(deck_init(46, "8", '♤', 8))
deck.append(deck_init(45, "7", '♤', 7))
deck.append(deck_init(44, "6", '♤', 6))
deck.append(deck_init(43, "5", '♤', 5))
deck.append(deck_init(42, "4", '♤', 4))
deck.append(deck_init(41, "3", '♤', 3))
deck.append(deck_init(40, "2", '♤', 2))
deck.append(deck_init(39, "A", '♡', 14))
deck.append(deck_init(38, "K", '♡', 13))
deck.append(deck_init(37, "Q", '♡', 12))
deck.append(deck_init(36, "J", '♡', 11))
deck.append(deck_init(35, "10", '♡', 10))
deck.append(deck_init(34, "9", '♡', 9))
deck.append(deck_init(33, "8", '♡', 8))
deck.append(deck_init(32, "7", '♡', 7))
deck.append(deck_init(31, "6", '♡', 6))
deck.append(deck_init(30, "5", '♡', 5))
deck.append(deck_init(29, "4", '♡', 4))
deck.append(deck_init(28, "3", '♡', 3))
deck.append(deck_init(27, "2", '♡', 2))
deck.append(deck_init(26, "A", '♧', 14))
deck.append(deck_init(25, "K", '♧', 13))
deck.append(deck_init(24, "Q", '♧', 12))
deck.append(deck_init(23, "J", '♧', 11))
deck.append(deck_init(22, "10", '♧', 10))
deck.append(deck_init(21, "9", '♧', 9))
deck.append(deck_init(20, "8", '♧', 8))
deck.append(deck_init(19, "7", '♧', 7))
deck.append(deck_init(18, "6", '♧', 6))
deck.append(deck_init(17, "5", '♧', 5))
deck.append(deck_init(16, "4", '♧', 4))
deck.append(deck_init(15, "3", '♧', 3))
deck.append(deck_init(14, "2", '♧', 2))
deck.append(deck_init(13, "A", '♢', 14))
deck.append(deck_init(12, "K", '♢', 13))
deck.append(deck_init(11, "Q", '♢', 12))
deck.append(deck_init(10, "J", '♢', 11))
deck.append(deck_init(9, "10", '♢', 10))
deck.append(deck_init(8, "9", '♢', 9))
deck.append(deck_init(7, "8", '♢', 8))
deck.append(deck_init(6, "7", '♢', 7))
deck.append(deck_init(5, "6", '♢', 6))
deck.append(deck_init(4, "5", '♢', 5))
deck.append(deck_init(3, "4", '♢', 4))
deck.append(deck_init(2, "3", '♢', 3))
deck.append(deck_init(1, "2", '♢', 2))


decknojoker = deck.copy()
decknojoker.pop(0)
deckwithjoker = deck.copy()
drawncardswithjoker = []
drawncardswithoutjoker = []
drawncard = []
class ThreeCardLogic:
	@classmethod
	def findhandvalue(cls, Hand):
		if (Hand[0].value == Hand[1].value -1 and Hand[1].value == Hand[2].value -1 or Hand[2].value == 14 and Hand[1].value == 3 and Hand[0].value == 2):
			if(Hand[0].suit == Hand[1].suit == Hand[2].suit):
				if(Hand[0].value == 14):
					handvalue = "Mini Royal Flush"
					return handvalue
				handvalue = "Straight Flush"
				return handvalue
			handvalue = "Straight"
			return handvalue
		if(Hand[0].suit == Hand[1].suit == Hand[2].suit):
			handvalue = "Flush"
			return handvalue
		if(Hand[0].value == Hand[1].value & Hand[0].value == Hand[2].value):
			handvalue = "Three of a Kind"
			return handvalue
		if(Hand[0].value == Hand[1].value or Hand[2].value == Hand[0].value or Hand[1].value == Hand[2].value):
			handvalue = "One Pair"
			return handvalue
		handvalue = "Garbaggio"
		return handvalue
	@classmethod
	def findwinner(cls,playerHand,dealerHand):
		Handlength = len(playerHand) - 1
		while(Handlength >= 0):
			if (playerHand[2].value > dealerHand[2].value):
				return 1
			if (playerHand[2].value == dealerHand[2].value):
				if (playerHand[1].value > dealerHand[1].value):
					return 1
			if (playerHand[1].value == dealerHand[1].value):
				if (playerHand[0].value > dealerHand[0].value):
					return 1
			if (playerHand[0].value == dealerHand[0].value):
				return 3
			else:
				return 0
	@classmethod
	def findhandtype(cls,HandType):
		if (HandType == "Mini Royal Flush"):
			return 7
		if (HandType == "Straight Flush"):
			return 6
		if (HandType == "Three of a Kind"):
			return 5
		if (HandType == "Straight"):
			return 4
		if (HandType == "Flush"):
			return 3
		if (HandType == "One Pair"):
			return 2
		if (HandType == "Garbaggio"):
			return 1		
	@classmethod
	def findsixcardvalue(cls, Hand):
		flatsuitarray = [card.suit for card in Hand]
		handcount = Counter(flatsuitarray)
		countsuitclub = handcount["♧"]
		countsuitdiamond = handcount["♢"]
		countsuitheart = handcount["♡"]
		countsuitspade = handcount["♤"]
		if (Hand[0].value == Hand[1].value -1 and Hand[1].value == Hand[2].value -1 and Hand[2].value == Hand[3].value -1 and Hand[3].value == Hand[4].value -1 or Hand[1].value == Hand[2].value -1 and Hand[2].value == Hand[3].value -1 and Hand[3].value == Hand[4].value -1 and Hand[4].value == Hand[5].value -1 or Hand[5].value == 14 and Hand[4].value == 5 and Hand[3].value == 4 and Hand[2].value == 3 and Hand[1].value == 2 or Hand[5].value == 14 and Hand[3].value == 5 and Hand[2].value == 4 and Hand[1].value == 3 and Hand[0].value == 2):
			if(countsuitspade >= 5 or countsuitheart >= 5 or countsuitdiamond >= 5 or countsuitclub >= 5):
				if(Hand[5].value == 14 and Hand[4].value == 13 and Hand[5].suit == Hand[4].suit):
					handvalue = "Royal Flush"
					return handvalue
				handvalue = "Straight Flush"
				return handvalue
			handvalue = "Straight"
			return handvalue
		if(countsuitspade >= 5 or countsuitheart >= 5 or countsuitdiamond >= 5 or countsuitclub >= 5):
			handvalue = "Flush"
			return handvalue
		flatrankarray = [card.value for card in Hand]
		rankcount = Counter(flatrankarray)
		countrankA = rankcount[14]
		countrankK = rankcount[13]
		countrankQ = rankcount[12]
		countrankJ = rankcount[11]
		countrank10 = rankcount[10]
		countrank9 = rankcount[9]
		countrank8 = rankcount[8]
		countrank7 = rankcount[7]
		countrank6 = rankcount[6]
		countrank5 = rankcount[5]
		countrank4 = rankcount[4]
		countrank3 = rankcount[3]
		countrank2 = rankcount[2]
		countrank = []
		countrank.append(countrankA), countrank.append(countrankK), countrank.append(countrankQ), countrank.append(countrankJ), countrank.append(countrank10), countrank.append(countrank9), countrank.append(countrank8), countrank.append(countrank7), countrank.append(countrank6), countrank.append(countrank5),countrank.append(countrank4),countrank.append(countrank3), countrank.append(countrank2)
		countranknoA = all(item >= 2 for index, item in enumerate(countrank) if index != 0)
		countranknoK = all(item >= 2 for index, item in enumerate(countrank) if index != 1)
		countranknoQ = all(item >= 2 for index, item in enumerate(countrank) if index != 2)
		countranknoJ = all(item >= 2 for index, item in enumerate(countrank) if index != 3)
		countrankno10 = all(item >= 2 for index, item in enumerate(countrank) if index != 4)
		countrankno9 = all(item >= 2 for index, item in enumerate(countrank) if index != 5)
		countrankno8 = all(item >= 2 for index, item in enumerate(countrank) if index != 6)
		countrankno7 = all(item >= 2 for index, item in enumerate(countrank) if index != 7)
		countrankno6 = all(item >= 2 for index, item in enumerate(countrank) if index != 8)
		countrankno5 = all(item >= 2 for index, item in enumerate(countrank) if index != 9)
		countrankno4 = all(item >= 2 for index, item in enumerate(countrank) if index != 10)
		countrankno3 = all(item >= 2 for index, item in enumerate(countrank) if index != 11)
		countrankno2 = all(item >= 2 for index, item in enumerate(countrank) if index != 12)
		if(countrankA >= 4 or countrankK >= 4 or countrankQ >= 4 or countrankJ >= 4 or countrank10 >= 4 or countrank9 >= 4 or countrank8 >= 4 or countrank7 >= 4 or countrank6 >=4 or countrank5 >=4 or countrank4 >= 4 or countrank3 >= 4 or countrank2 >= 4):
			handvalue = "Four of a Kind"
			return handvalue
		if(countrankA >= 3 and countranknoA == True or countrankK >= 3 and countranknoK == True or countrankQ >= 3 and countranknoQ == True or countrankJ >= 3 and countranknoJ == True or countrank10 >= 3 and countrankno10 == True or countrank9 >= 3 and countrankno9 == True or countrank8 >= 3 and countrankno8 == True or countrank7 >= 3 and countrankno7 == True or countrank6 >=3 and countrankno6 == True or countrank5 >= 3 and countrankno5 == True or countrank4 >= 3 and countrankno4 == True or countrank3 >= 3 and countrankno3 == True or countrank2 >= 3 and countrankno2 == True):
			handvalue = "Full House"
			return handvalue
		if(countrankA >= 3 or countrankK >= 3 or countrankQ >= 3 or countrankJ >= 3 or countrank10 >= 3 or countrank9 >= 3 or countrank8 >= 3 or countrank7 >= 3 or countrank6 >= 3 or countrank5 >= 3 or countrank4 >= 3 or countrank3 >= 3 or countrank2 >= 3):
			handvalue = "Three of a Kind"
			return handvalue
		else:
			handvalue = "Garbaggio"
			return handvalue
	@classmethod
	def findsixcardtype(cls,HandType):
		if (HandType == "Royal Flush"):
			return 8
		if (HandType == "Straight Flush"):
			return 7
		if (HandType == "Four of a Kind"):
			return 6
		if (HandType == "Full House"):
			return 5
		if (HandType == "Flush"):
			return 4
		if (HandType == "Straight"):
			return 3
		if (HandType == "Three of a Kind"):
			return 2
		if (HandType == "Garbaggio"):
			return 1	

class DrawCardsNoJoker:
	@classmethod
	def draw_cards(cls,totalCards, amountofcardstodraw):
		while amountofcardstodraw > 0:
			drawncard = (random.choice(decknojoker))
			while(drawncard in totalCards):
				drawncard = (random.choice(decknojoker))
			totalCards.append(drawncard)
			amountofcardstodraw -= 1

class DrawCardsWithJoker:
	@classmethod
	def draw_cards(cls, amountofcardstodraw):
		while amountofcardstodraw > 0:
			drawncard = (random.choice(deckwithjoker))
			deckwithjoker.remove(drawncard)
			drawncardswithjoker.append(drawncard)
			amountofcardstodraw -= 1

class ThreeCardPoker:
	def play():
		bankroll = ""
		print("Welcome to Three Card Poker")
		print("What would you like to do? (Payouts) to show payouts,(Auto) to enable automatic mode, or (Exit) to quit")
		menuoption = input()
		if (menuoption == "Payouts"):
			print("The payouts for Three Card Poker are as follows:")
			print("\nSix Card Bonus-")
			print("Royal Flush:         1,000 to 1")
			print("Straight Flush:      200 to 1")
			print("Four of a Kind:      100 to 1")
			print("Full House:          20 to 1")
			print("Flush:               15 to 1")
			print("Straight:            10 to 1")
			print("Three of a Kind:     7 to 1")
			print("\nPairs Plus Bonus-")
			print("Royal Flush:         200 to 1")
			print("Straight Flush:      40 to 1")
			print("Three of a Kind:     30 to 1")
			print("Straight:            6 to 1")
			print("Flush:               3 to 1")
			print("One Pair:            1 to 1")
			print("\nAnte Bonus-")
			print("Straight Flush:      5 to 1")
			print("Three of a Kind:     4 to 1")
			print("Straight:            1 to 1")
			ThreeCardPoker.play()
		if (menuoption == "Play"):
			def threecardmain():
				bankroll = input("How much starting bankroll would you like? ")
				bankroll = int(bankroll)
				while (bankroll > 10):
					print(f"You have {bankroll} remaining.")
					dealerqualify = 0
					totalCards = []
					playerHand = []
					dealerHand = []
					ante = input("How much would you like to bet on the Ante? ")
					ante = int(ante)
					pairsplus = input("How much would you like to bet on the Pairs Plus? ")
					pairsplus = int(pairsplus)
					sixcardbonus = input("How much would you like to bet on the six card bonus? ")
					sixcardbonus = int(sixcardbonus)
					if (ante * 2 + pairsplus + sixcardbonus > bankroll):
						print("Error, you do not have enough money to place your bets in this configuration and play your ante bet, please try again.")
						threecardmain()
					bankroll -= ante
					bankroll -= pairsplus
					bankroll -= sixcardbonus
					DrawCardsNoJoker.draw_cards(totalCards,6)
					playerHand.append(totalCards[0])
					playerHand.append(totalCards[1])
					playerHand.append(totalCards[2])
					dealerHand.append(totalCards[3])
					dealerHand.append(totalCards[4])
					dealerHand.append(totalCards[5])
					antebonustotalbonus = 0
					totalCards = sorted(totalCards, key=lambda card: card.value)
					playerHand = sorted(playerHand, key=lambda card: card.value)
					dealerHand = sorted(dealerHand, key=lambda card: card.value)
					playerHandValue = ThreeCardLogic.findhandvalue(playerHand)
					dealerHandValue = ThreeCardLogic.findhandvalue(dealerHand)
					sixcardHandValue = ThreeCardLogic.findsixcardvalue(totalCards)
					sixcardhandtype = ThreeCardLogic.findsixcardtype(sixcardHandValue)
					playerhandtype = ThreeCardLogic.findhandtype(playerHandValue)
					dealerhandtype = ThreeCardLogic.findhandtype(dealerHandValue)
					print("You have:")
					for card in playerHand:
						print(f"{card.rank} of {card.suit}")
					if (playerhandtype > 1):
						print(f"Which is {playerHandValue}")
					FoldFlag = input("Would you like to (Play) this hand, or (Fold)? You still get paid for bonuses regardless ")
					if (FoldFlag == "Play"):
						if (dealerHand[0].value < 12 and dealerHand[1].value < 12 and dealerHand[2].value < 12):
							dealerqualify = 0
						else:
							dealerqualify = 1
						if (dealerqualify == 0):
							print("The dealer does not qualify. Your play bet has been returned and your Ante is a win")
						if (dealerHandValue == playerHandValue):
							playerwin = ThreeCardLogic.findwinner(playerHand,dealerHand)
						else:
							if (playerhandtype > dealerhandtype):
								playerwin = 1
							else:
								playerwin = 0
						print("The Dealer Has")
						for card in dealerHand:
							print(f"{card.rank} of {card.suit}")
						if (dealerhandtype > 1):
							print(dealerHandValue)
						else:
							print(f"The Dealer has {dealerHand[2].rank} high")
						print("The Player Has")
						for card in playerHand:
							print(f"{card.rank} of {card.suit}")
						if (playerhandtype > 1):
							print(playerHandValue)
						else:
							print(f"The Player has {playerHand[2].rank} high")
						if (playerwin == 1 or playerwin == 0 and dealerqualify == 0 or playerwin == 3 and dealerqualify == 0):
							print("The Player wins")
							ante = ante + ante
							if (playerwin == 1 and dealerqualify == 1):
								if (playerhandtype > 3):
									if (playerhandtype == 7 or playerhandtype == 6):
										antebonus = 5
									if (playerhandtype == 5):
										antebonus = 4
									if (playerhandtype == 4):
										antebonus = 1
									antebonustotalbonus = ante * antebonus
									print(f"You have hit an ante bonus hand. You will be paid {antebonus} times your Ante Bet for an additional {antebonustotalbonus}")
								ante = ante * 4
					if (playerwin == 0 and dealerqualify == 1):
						print("The Dealer wins")
						ante = 0
					if (playerwin == 3 and dealerqualify == 1):
						print("The hand is a push")
					if (playerwin == 1 and dealerqualify == 0 or playerwin == 0 and dealerqualify == 0):
						ante = ante * 2
					if (FoldFlag == "Fold"):
						if (dealerHand[0].value < 12 and dealerHand[1].value < 12 and dealerHand[2].value < 12):
							dealerqualify = 0
						else:
							dealerqualify = 1
						if (dealerhandtype > 1):
							dealerqualify = 1
						if (dealerqualify == 0):
							print("The dealer did not qualify.")
						if (dealerHandValue == playerHandValue):
							playerwin = ThreeCardLogic.findwinner(playerHand,dealerHand)
						else:
							if (playerhandtype > dealerhandtype):
								playerwin = 1
							else:
								playerwin = 0
						print("The Dealer Had")
						for card in dealerHand:
							print(f"{card.rank} of {card.suit}")
						if (dealerhandtype > 1):
							print(dealerHandValue)
						else:
							print(f"The Dealer had {dealerHand[2].rank} high")
						print("The Player Had")
						for card in playerHand:
							print(f"{card.rank} of {card.suit}")
						if (playerhandtype > 1):
							print(playerHandValue)
						else:
							print(f"The Player had {playerHand[2].rank} high")
						if (playerwin == 1 or playerwin == 0 and dealerqualify == 0 or playerwin == 3 and dealerqualify == 0):
							print("The Player would have won")
							ante = ante + ante
							if (playerwin == 1 and dealerqualify == 1):
								if (playerhandtype > 3):
									if (playerhandtype == 7 or playerhandtype == 6):
										antebonus = 0
									if (playerhandtype == 5):
										antebonus = 0
									if (playerhandtype == 4):
										antebonus = 0
									antebonustotalbonus = ante * antebonus
								ante = ante * 2

						if (playerwin == 0 and dealerqualify == 1):
							print("The Dealer wins")
							ante = 0
						if (playerwin == 3 and dealerqualify == 1):
							print("The hand is a push")
					if (playerhandtype > 1):
						if (playerhandtype == 7):
							pairsplusbonuspayout = 200
						if (playerhandtype == 6):
							pairsplusbonuspayout = 40
						if (playerhandtype == 5):
							pairsplusbonuspayout = 30
						if (playerhandtype == 4):
							pairsplusbonuspayout = 6
						if (playerhandtype == 3):
							pairsplusbonuspayout = 3
						if (playerhandtype == 2):
							pairsplusbonuspayout = 1
						pairsplustotalbonus = pairsplus * pairsplusbonuspayout
						print(f"You have hit a bonus hand. You will be paid {pairsplusbonuspayout} times your Pairs Plus Bonus Bet for an additional {pairsplustotalbonus}")
					else:
						print("No Pairs Plus bonus has been hit.")
						pairsplus = 0
						pairsplustotalbonus = 0
						antebonustotalbonus = 0
					sixcardhandtype = ThreeCardLogic.findsixcardtype(sixcardHandValue)
					if (sixcardhandtype > 1):
						if (sixcardhandtype == 8):
							sixcardbonuspayout = 1000
						if (sixcardhandtype == 7):
							sixcardbonuspayout = 200
						if (sixcardhandtype == 6):
							sixcardbonuspayout = 100
						if (sixcardhandtype == 5):
							sixcardbonuspayout = 20
						if (sixcardhandtype == 4	):
							sixcardbonuspayout = 15
						if (sixcardhandtype == 3):
							sixcardbonuspayout = 10
						if (sixcardhandtype == 2):
							sixcardbonuspayout = 7	
						sixcardtotalbonus = sixcardbonus * sixcardbonuspayout
						print(f"You have hit a bonus hand. You will be paid {sixcardbonuspayout} times your Six Card Bonus Bet for an additional {sixcardtotalbonus} for your {sixcardHandValue}!")
					else:
						print("No Six Card bonus has been hit.")
						sixcardbonus = 0
						sixcardbonuspayout = 0
						sixcardtotalbonus = 0
					bankroll = bankroll + pairsplus + pairsplustotalbonus + sixcardbonus + ante + antebonustotalbonus + sixcardtotalbonus
			threecardmain()
		if (menuoption == "Auto"):
			def threecardauto():
				handcounter = input("How many hands would you like to play? ")
				handcounter = int(handcounter)
				bankroll = input("How much starting bankroll would you like? ")
				bankroll = int(bankroll)
				ante = input("How much would you like to bet on the Ante? ")
				ante = int(ante)
				pairsplus = input("How much would you like to bet on the Pairs Plus? ")
				pairsplus = int(pairsplus)
				sixcardbonus = input("How much would you like to bet on the six card bonus? ")
				sixcardbonus = int(sixcardbonus)
				optimalstrategy = input("Do you want to play with optimal strategy?, folding hands lower than Q 6 4 (Y/N)")
				if (optimalstrategy == "Y"):
					optimalmodeon = True
				else:
					optimalmodeon = False
				martingale = input("Do you want to play with a martingale ante? (Y/N)")
				if (martingale == "Y"):
					martingaleon = True
				else:
					martingaleon = False
				initsixcardbonus = sixcardbonus
				initpairsplus = pairsplus
				initante = ante
				martingaleante = ante
				losscounter = False
				while (handcounter != 0):
					sixcardbonus = initsixcardbonus
					pairsplus = initpairsplus
					if (martingaleon == False):
						ante = initante
					if (martingaleon == True):
						ante = martingaleante
						if (losscounter == True):
							ante = ante * 2
					martingaleante = ante
					print(f"You have {bankroll} remaining.")
					dealerqualify = 0
					totalCards = []
					playerHand = []
					dealerHand = []
					playerhandtype = 0
					dealerhandtype = 0
					bankroll -= ante
					bankroll -= pairsplus
					bankroll -= sixcardbonus
					DrawCardsNoJoker.draw_cards(totalCards,6)
					playerHand.append(totalCards[0])
					playerHand.append(totalCards[1])
					playerHand.append(totalCards[2])
					dealerHand.append(totalCards[3])
					dealerHand.append(totalCards[4])
					dealerHand.append(totalCards[5])
					antebonustotalbonus = 0
					totalCards = sorted(totalCards, key=lambda card: card.value)
					playerHand = sorted(playerHand, key=lambda card: card.value)
					dealerHand = sorted(dealerHand, key=lambda card: card.value)
					playerHandValue = ThreeCardLogic.findhandvalue(playerHand)
					dealerHandValue = ThreeCardLogic.findhandvalue(dealerHand)
					sixcardHandValue = ThreeCardLogic.findsixcardvalue(totalCards)
					sixcardhandtype = ThreeCardLogic.findsixcardtype(sixcardHandValue)
					playerhandtype = ThreeCardLogic.findhandtype(playerHandValue)
					dealerhandtype = ThreeCardLogic.findhandtype(dealerHandValue)
					if (optimalmodeon == True):
						if (playerhandtype <= 2):
							if (playerHand[2].value < 12):
								bankroll -= ante
								losscounter = True
								continue
							if (playerHand[2].value == 12):
								if (playerHand[1].value < 6):
									bankroll -= ante
									losscounter = True
									continue
							if (playerHand[2].value == 12):
								if (playerHand[1].value == 6):
									if (playerHand[0].value < 4):
										bankroll -= ante
										losscounter = True
										continue
					print("You have:")
					for card in playerHand:
						print(f"{card.rank} of {card.suit}")
					if (playerhandtype > 1):
						print(f"Which is {playerHandValue}")
					else:
						print(f"Which is {playerHand[2].rank} high")
					if (dealerHand[0].value < 12 and dealerHand[1].value < 12 and dealerHand[2].value < 12):
						dealerqualify = 0
					else:
						dealerqualify = 1
					if (dealerhandtype > 1):
						dealerqualify = 1
					if (dealerqualify == 0):
						print("The dealer does not qualify. Your play bet has been returned and your Ante is a win")
					if (dealerHandValue == playerHandValue):
						playerwin = ThreeCardLogic.findwinner(playerHand,dealerHand)
					else:
						if (playerhandtype > dealerhandtype):
							playerwin = 1
						else:
							playerwin = 0
					print("The Dealer Has")
					for card in dealerHand:
						print(f"{card.rank} of {card.suit}")
					if (dealerhandtype > 1):
						print(dealerHandValue)
					else:
						print(f"The Dealer has {dealerHand[2].rank} high")
					if (playerwin == 1 or playerwin == 0 and dealerqualify == 0 or playerwin == 3 and dealerqualify == 0):
						print("The Player wins")
						losscounter = False
						martingaleante = initante
						if (playerwin == 1 and dealerqualify == 1):
							if (playerhandtype > 3):
								if (playerhandtype == 7 or playerhandtype == 6):
									antebonus = 5
								if (playerhandtype == 5):
									antebonus = 4
								if (playerhandtype == 4):
									antebonus = 1
								antebonustotalbonus = ante * antebonus
								ante = ante * 4
								print(f"You have hit an ante bonus hand. You will be paid {antebonus} times your Ante Bet for an additional {antebonustotalbonus}")
					if (playerwin == 0 and dealerqualify == 1):
						print("The Dealer wins")
						losscounter = True
						ante = 0
					if (playerwin == 3 and dealerqualify == 1):
						print("The hand is a push")
					if (playerwin == 1 and dealerqualify == 0 or playerwin == 0 and dealerqualify == 0):
						ante = ante * 2
					if (playerhandtype > 1):
						if (playerhandtype == 7):
							pairsplusbonuspayout = 200
						if (playerhandtype == 6):
							pairsplusbonuspayout = 40
						if (playerhandtype == 5):
							pairsplusbonuspayout = 30
						if (playerhandtype == 4):
							pairsplusbonuspayout = 6
						if (playerhandtype == 3):
							pairsplusbonuspayout = 3
						if (playerhandtype == 2):
							pairsplusbonuspayout = 1
						pairsplustotalbonus = pairsplus * pairsplusbonuspayout
						print(f"You have hit a bonus hand. You will be paid {pairsplusbonuspayout} times your Pairs Plus Bonus Bet for an additional {pairsplustotalbonus}")
					else:
						print("No Pairs Plus bonus has been hit.")
						pairsplus = 0
						pairsplustotalbonus = 0
					sixcardhandtype = ThreeCardLogic.findsixcardtype(sixcardHandValue)
					if (sixcardhandtype > 1):
						if (sixcardhandtype == 8):
							sixcardbonuspayout = 1000
						if (sixcardhandtype == 7):
							sixcardbonuspayout = 200
						if (sixcardhandtype == 6):
							sixcardbonuspayout = 100
						if (sixcardhandtype == 5):
							sixcardbonuspayout = 20
						if (sixcardhandtype == 4	):
							sixcardbonuspayout = 15
						if (sixcardhandtype == 3):
							sixcardbonuspayout = 10
						if (sixcardhandtype == 2):
							sixcardbonuspayout = 7	
						sixcardtotalbonus = sixcardbonus * sixcardbonuspayout
						print(f"You have hit a bonus hand. You will be paid {sixcardbonuspayout} times your Six Card Bonus Bet for an additional {sixcardtotalbonus} for your {sixcardHandValue}!")
					else:
						print("No Six Card bonus has been hit.")
						sixcardbonus = 0
						sixcardbonuspayout = 0
						sixcardtotalbonus = 0
					bankroll = bankroll + pairsplus + pairsplustotalbonus + sixcardbonus + ante + antebonustotalbonus + sixcardtotalbonus
					handcounter = handcounter - 1
			threecardauto()

class MainMenu:
	print("Welcome to the main menu, please choose a game.\n Avaliable Games: \n Three Card Poker")
	gamechoice = input()
	if (gamechoice == "Three Card Poker"):
		ThreeCardPoker.play()

MainMenu()