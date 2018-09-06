import random

class coinToss(object):
	def __init__(self,player1,player2):
		self.player1 = player1
		self.player2 = player2


	def round(self):
		events = ["heads", "tails"]
		coinFace = random.choice(events)
		if self.player1 == 0 or self.player2 == 0 :
			return self.player1, self.player2
		else:
			if coinFace == "heads":
				self.player1 += 100
				self.player2 -= 100
			else:
				self.player2 += 100
				self.player1 -= 100
			return self.player1, self.player2
		




game = coinToss(1000,1000)
file1 = open("player1.dat","w+")
file1.write("#Player 1 \n")
file1.write("#Money Round \n")
file2 = open("player2.dat", "w+")
file2.write("#Player 2 \n")
file2.write("#Money Round \n")
for i in range(0, 1001):
	game.player1,game.player2 = game.round()
	file1.write(str(game.player1) + " " + str(i) + "\n")
	file2.write(str(game.player2) + " " + str(i) + "\n")



	





