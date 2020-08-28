import requests
from bs4 import BeautifulSoup as bs

print("*** Page Scraper ***")

page = requests.get(input("Full url: "))
cleaned = bs(page.content, "html.parser")

images = cleaned.find_all("img")
for i in images:
	title, source = i.find("img", class_="alt"), i.find("img", class_="src")
	if None in (title, source):
		continue
	print(title.text, source.text)
	# TODO: Fix 56
