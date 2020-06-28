import re

print("*** Regex Query Tool ***")

print("Match" if re.search(input("Pattern: "), input("String: ")) else "No Match")
