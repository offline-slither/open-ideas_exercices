from random import randint


class Turn_order_class():
	def __init__(self,base_turn_order):
		self.core = base_turn_order
		self.total_turn = 0
		self.mini_turn_count = 0
		self.hold = []
	def to_display(self):
		print(f"c'est le tour de {self.core[0][1]}")
		print(self.core)
	def moveon(self):
		trv = self.core.pop(0)
		self.core.append(trv)
	def next(self):
		if len(self.core) <= 1:
			print("-----*le combat est terminé*-----")
			return
		current.moveon()
		current.to_display()
		self.mini_turn_count += 1
		if self.mini_turn_count >= len(self.core):
			self.mini_turn_count = 0
			self.total_turn += 1
			print(f"{self.total_turn} tour global est passé")
	def on_hold(self):
		self.hold.append(self.core.pop(0))
		current.to_display()
		if self.mini_turn_count >= len(self.core):
			self.mini_turn_count = 0
			self.total_turn += 1
			print(f"{self.total_turn} tour global est passé")
	def off_hold(self,holdvalue=0):
		self.core.insert(0,self.hold[holdvalue])
		print(f"{self.core[0][1]} qui avais retadé son tour rejoins et effectue son action")
		current.to_display()




Characters = [["Unit",6,"unit.jpg"],["Tic",12,"Tic.jpg"],["Kadwalon",12,"Kad.jpg"],["Eldrod",4,"ElfWyzard.jpg"],["Ludwig",5,"mechani.jpg"]]
base_turn_order = []
count = 0
for hero in Characters:
  Score = Characters[count][1] + randint(1,20)
  base_turn_order.append([Score,Characters[count][0]])
  count += 1

base_turn_order = (list(reversed(sorted(base_turn_order))))
# print(base_turn_order)

current = Turn_order_class(base_turn_order)
current.to_display()
