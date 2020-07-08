import datetime

print("*** What's the day ***")


def leap(n: int):
	if (n % 4) == 0:
		if (n % 100) == 0:
			if (n % 400) == 0:
				return True
			else:
				return False
		else:
			return True
	else:
		return False


def day(year: int, month: int, day: int):
	try:
		print(datetime.date(year, month, day).strftime("%A %d. %B %Y"))
	except ValueError:
		print("Not a real date")
