import json

print("*** Text-Speak Converter ***")

with open("Text-Speak Converter.json", 'r') as f:
	lst = json.load(f)

if input("Add new value? (y/n) ").lower() == "y":
	lst[input("Abbreviation: ")] = input("Words: ")
	with open("Text-Speak Converter.json", 'w') as f:
		json.dump(lst, f)

print(lst[input("Abbreviation: ")])
