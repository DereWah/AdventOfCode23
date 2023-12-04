

max_red = 12
max_green = 13
max_blue = 14
valid_games = 0
min_power = 0


f = open("input.txt", "r")

games = f.read().splitlines()

data = []



class SingleSet:
	green = 0
	red = 0
	blue = 0
	
	def __init__(self, text):
		text = text.split(", ")
		for dices in text:
			if "red" in dices:
				dices = dices.replace("red", "")
				self.red = int(dices)
			elif "green" in dices:
				dices = dices.replace("green", "")
				self.green = int(dices)
			elif "blue" in dices:
				dices = dices.replace("blue", "")
				self.blue = int(dices)
			
	def is_valid_set(self):
		return (self.green <= max_green and
			self.red <= max_red and
			self.blue <= max_blue)

			
class Game:
	index = 0
	sets = []
	
	def __init__(self, text, i):
		self.sets = []
		self.index = i
		text = text.replace(f"Game {self.index}: ", "")
		text = text.split(";")
		for s in text:
			single_set = SingleSet(s)
			self.sets.append(single_set)
			
			
	def is_valid_game(self):
		for s in self.sets:
			if not s.is_valid_set():
				return False
		return True
		
	def minimum_to_be_valid(self):
		min_red = 0
		min_blue = 0
		min_green = 0
		for s in self.sets:
			if s.red > min_red:
				min_red = s.red
			if s.green > min_green:
				min_green = s.green
			if s.blue > min_blue:
				min_blue = s.blue
		return min_red*min_blue*min_green
			
		


for i, g in enumerate(games):
	new_game = Game(g, i+1)
	data.append(new_game)
	
for game in data:
	valid = game.is_valid_game()
	if(valid):
		valid_games += game.index
	min_power += game.minimum_to_be_valid()
		
print(f"Valid games: {valid_games}")
print(f"Min: {min_power}")


	
