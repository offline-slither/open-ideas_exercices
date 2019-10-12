from bs4 import BeautifulSoup
import requests
from random import choice
from time import sleep
base_url = "https://www.viedemerde.fr/?page="
url = 1
# res = requests.get(f"{base_url}{url}")
# soup = bs4.BeautifulSoup(resp.text, "html.parser")
panel = []
# --------------------quote recuperation logic -------------------------
# urlcount = 1
for numba in range(1,5):
	print(f"Scrapping {base_url}{str(url)}..........")
	res = requests.get(f"{base_url}{url}")
	print("done")
	soup = BeautifulSoup(res.text, "html.parser")
	des_contents = soup.find_all(class_="panel panel-classic")

	for story in des_contents:
		panel.append({

			"text":story.find(class_="article-link").get_text(),
			"Title":story.find("h2").get_text(),
			"article-link" : story.find("a")["href"]
			})

		# next_btn = soup.find(class_="text-center")
		# url = next_btn.find(class_="jscroll-next btn btn-primary btn-lg")["href"]
		# print(des_contents)
	url += 1
	# print(panel)
cite = choice(panel)
print(cite["text"],cite["article-link"] )
sleep(1)