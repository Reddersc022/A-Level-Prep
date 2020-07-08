import json

print("*** Speed Tracker ***")

time1, time2, reg = int(input("Start time (s): ")), int(input("End time (s): ")), input("Registration (xxxx xxx): ")
timeBool, regBool = False, False

if len(reg) == 8 and reg[0:2].isalpha() and reg[2:4].isnumeric() and reg[5:-1].isalpha():
	regBool = True

if time2 - time1 >= 51:  # 70mph, over 1 mile
	timeBool = True

print("Registration is %s, speed is %s" % ("valid" if regBool else "invalid", "valid" if timeBool else "invalid"))

with open("Speed Tracker.json", 'r') as f:
	lst = json.load(f)

lst.append([reg, regBool, timeBool])

with open("Speed Tracker.json", 'w') as f:
	json.dump(lst, f)
