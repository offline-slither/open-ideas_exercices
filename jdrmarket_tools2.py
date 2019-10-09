import random
from termcolor import colored

inventory = {
	'canif': 95,
	'Gant de combat' : 100,
	'Matraque' : 90,
	'Epée de duel ': 475,
	'couteau suisse avancé' : 6000,
	'Epée à lame vibrante' : 9500,
	'Gant de combat à energie' : 16100,
	'Falchion a lame ultra fine' : 2600,
	'Dague trachant atomique' : 32800


}


# nom_item,  keyprice CR (en rouge) valeur promo = prix calculé

def marketmaker():
	for each in inventory :
		is_there = random.randrange(1,11)
		# print(f"is_there{is_there}")
		if is_there <= 3:
			pass
		else:
			promoval = random.randrange(1,101)
			if promoval == 42 :
				applied = 70
			elif promoval >= 50 :
				applied = 20
			elif promoval >19 & promoval < 50:
				applied = 30
			elif promoval >4 & promoval <= 19:
				applied = 40
			else:
				applied = 50
			status = "regular"
			marqueur = random.randrange(1,11)
			# print(marqueur)
			if marqueur <= 3:
				status = " promo"
				# print(f"{each},{inventory[each]} CR,{colored(status, color='green')}, -{applied}% = {inventory[each]-((inventory[each] / 100)* applied)} CR")
				print(f"{each},{inventory[each]} CR,{status}, -{applied}% = {inventory[each]-((inventory[each] / 100)* applied)} CR")
			elif marqueur == 4:
				status = " quasi-rupture"
				# print(f"{each},{inventory[each]} CR,{colored(status, color='red')}, + {applied}% = {inventory[each]+((inventory[each] / 100)* applied)} CR")
				print(f"{each},{inventory[each]} CR,{status}, + {applied}% = {inventory[each]+((inventory[each] / 100)* applied)} CR")

			else:
				status = " regular"
				print(f"{each},{inventory[each]}")


marketmaker()

# promoval = random.randrange(1,101)
# if promoval == 42 :
# 	applied = 70
# elif promoval >= 50 :
# 	applied = 20
# elif promoval >19 & promoval < 50:
# 	applied = 30
# elif promoval >4 & promoval <= 19:
# 	applied = 30
# else:
# 	applied = 70