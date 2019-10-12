import random
import csv
from termcolor import colored

page_output = False
# page_output determine si une page exterieure sera generée en plus de l'inventaire il est désactivé par défault

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

# alt: read from cvs, attend un CVS comportant des données  nom objet, prix(int), voir pre-list fournis comme exemple

readdict = {}
with open("pre-list.cvs") as file:
	csv_reader = csv.reader(file)
	for row in csv_reader:
		readdict.update( {f"{row[0]}" : row[1]} )




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

def fromlist_marketmaker():
	if page_output == True: Nom_fichier = input("name of the file ?")

	for each in readdict :
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
				if page_output == True:
					with open(Nom_fichier,"a") as file:
						csv_writer = csv.writer(file)
						text_result = f"{each},{readdict[each]} CR,{status}, -{applied}% = {int(readdict[each])-((int(readdict[each]) / 100)* applied)} CR"
						# csv_writer.writerow(f"{each},{readdict[each]} CR,{colored(status, color='green')}, -{applied}% = {int(readdict[each])-((int(readdict[each]) / 100)* applied)} CR")
						csv_writer.writerow([text_result])
				status = "promo"
				print(f"{each},{readdict[each]} CR,{colored(status, color='green')}, -{applied}% = {int(readdict[each])-((int(readdict[each]) / 100)* applied)} CR")
				# print(f"{each},{readdict[each]} CR,{status}, - {applied}% = {readdict[each]-((readdict[each] / 100)* applied)} CR")
			elif marqueur == 4:
				if page_output == True:
					with open(Nom_fichier,"a") as file:
						csv_writer = csv.writer(file)
						text_result = f"{each},{readdict[each]} CR,{status}, + {applied}% = {int(readdict[each])+((int(readdict[each]) / 100)* applied)} CR"
						# csv_writer.writerow(f"{each},{readdict[each]} CR,{colored(status, color='red')}, + {applied}% = {int(readdict[each])+((int(readdict[each]) / 100)* applied)} CR")
						csv_writer.writerow([text_result])
				status = " quasi-rupture"
				print(f"{each},{readdict[each]} CR,{colored(status, color='red')}, + {applied}% = {int(readdict[each])+((int(readdict[each]) / 100)* applied)} CR")
				# print(f"{each},{readdict[each]} CR,{status}, + {applied}% = {readdict[each]+((readdict[each] / 100)* applied)} CR")

			else:
				if page_output == True:
					with open(Nom_fichier,"a") as file:
						csv_writer = csv.writer(file)
						text_result = f"{each},{readdict[each]}"
						csv_writer.writerow([text_result])
						# csv_writer.writerow(f"{each},{readdict[each]}")
				status = " regular"
				print(f"{each},{readdict[each]}")

# you'v to swap commented line with there supérior, so you can have promo and non-promo in colored text


# alt: write from cvs
# with open("new_shop.cvs","w") as file:
# 	csv_writer = csv.writer(file)
# 	csv_writer.writerow(f"{each},{readdict[each]} CR,{colored(status, color='green')}, -{applied}% = {int(readdict[each])-((int(readdict[each]) / 100)* applied)} CR")

# fromlist_marketmaker()
# marketmaker()