print("*** Your Name is... ***")

msg = "Your name is %s, you are %s years old, and you are in form %s." \
	% (input("Name: "), input("Age: "), input("Form: "))

print(msg)

with open("Your Name is....txt", "a") as f:
	f.write("\n"+msg)
