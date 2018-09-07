import random

class coinToss(object):
	def __init__(self,player1,player2):
		self.player1 = player1
		self.player2 = player2


	def round(self):
		events = ["heads", "tails"]
		coinFace = random.choice(events)
		if coinFace == "heads":
			self.player1 += 100
			self.player2 -= 100
		else:
			self.player2 += 100
			self.player1 -= 100
		return self.player1, self.player2
	def reset(self):
		self.player1 = 100000
		self.player2 = 10000
		return self.player1, self.player2





game = coinToss(100000,10000)
fileGame = open("games.dat","w+")
fileGame.write("#Rodadas em cada Jogo\n")
fileGame.write("#NRounds Game \n")
tot = 0
i = 0
maximo = 0
for x in range(1,101):
	while (game.player1 != 0) and (game.player2 != 0):
		i += 1 
		game.player1,game.player2 = game.round()
	fileGame.write(str(i) + " " + str(x) + "\n")
	game.player1, game.player2 = game.reset()
	print "Jogo " + str(x)
	tot += i
	if maximo < i:
		maximo = i
	i = 0
	continue
print (tot/100)
print maximo









	





