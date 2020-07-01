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


# TODO: What's the day
