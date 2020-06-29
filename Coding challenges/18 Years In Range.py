print("*** Years In Range ***")

print(sum([1 for year in range(int(input("Year 1: ")), int(input("Year 2: "))) if len(list(dict.fromkeys(
	[i for i in str(year)]))) != 4]))
