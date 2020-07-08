import json

print("*** Event Calendar ***")

with open("Event Calendar.json", "r") as f:
	lst = json.load(f)

while input("Do you want to add more dates? (y/n) ").lower() == "y":
	date = input("Date (ddmmyyyy): ")
	if lst[date]:
		print("There is already an event on this day")
	else:
		lst[date] = input("Event: ")

while input("Do you want to delete any dates? (y/n) ").lower() == "y":
	del lst[input("Date (ddmmyyyy): ")]

[print(i, lst[i]) for i in lst]

with open("Event Calendar.json", "w") as f:
	json.dump(lst, f)
