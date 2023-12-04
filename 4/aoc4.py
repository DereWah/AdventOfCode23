

f = open("input.txt", "r")
lines = f.read().splitlines()
f.close()

total_scratch_cards = []

new_scratch_cards_pile = []

total_value = 0



class Card:
	index = 0
	winning = []
	current = []
	
	def __init__(self, text, i):
		self.winning = []
		self.current = []
		self.index = i
		text = text.replace("Card", "")
		text = text.replace(f"{i}:", "")
		text = text.split(" | ")
		wins = text[0].split(" ")
		currs = text[1].split(" ")
		for num in wins:
			if(num != ""):
				self.winning.append(int(num))
			
		for num in currs:
			if(num != ""):
				self.current.append(int(num))
			
	def get_value(self):
		count = -1
		for num in self.current:
			if num in self.winning:
				count += 1
		if(count != -1):
			return 2**(count)
		return 0
		
	def get_winning_amount(self):
		count = 0
		for num in self.current:
			if num in self.winning:
				count += 1
		return count
		
		
for i, l in enumerate(lines):
	card = Card(l, i+1)
	total_value += card.get_value()
	total_scratch_cards.append(card)
	new_scratch_cards_pile.append(1)
	
for id, amount in enumerate(new_scratch_cards_pile):
	winnings = total_scratch_cards[id].get_winning_amount()
	for i in range(id+1, id+winnings+1):
		if(i < len(new_scratch_cards_pile)):
			new_scratch_cards_pile[i] += amount
		
print(total_value)

print(sum(new_scratch_cards_pile))
