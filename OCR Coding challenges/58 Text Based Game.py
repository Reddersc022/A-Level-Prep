print("*** Text Based Game ***")


class Game:
	def __init__(self, name: str):
		self.name = name
		self.hasKey = False
		self.doorOpen = False

	def room1(self):
		print("Welcome, %s\nRoom 1:\nIn this room there is only a bed" % self.name)
		while True:
			choice = int(input("Do you:\n1. Move to room 2\n2. Quit\n%s: " % ("3. Use the secret door" if self.doorOpen else "")))
			if choice == 1:
				self.room2()
			elif choice == 2:
				quit()
			elif choice == 3:
				if self.doorOpen:
					self.room3()
				else:
					print("Not unlocked yet")
			else:
				print("Choose a correct option")

	def room2(self):
		print("Room 2:\nIn this room there is a chest, whispering %s" % self.name)
		while True:
			choice = int(input("Do you:\n1. Move to room 1\n2. Move to room 3\n3. Open the chest\n4. Quit\n: "))
			if choice == 1:
				self.room1()
			elif choice == 2:
				self.room3()
			elif choice == 3:
				print("You found a key!")
				self.hasKey = True
			elif choice == 4:
				quit()
			else:
				print("Choose a correct option")

	def room3(self):
		print("Room 3:\nIn this room, you see a secret door")
		while True:
			choice = int(input("Do you:\n1. Move to room 2\n2. Move to room 4\n3. Use the secret door\n4. Quit\n: "))
			if choice == 1:
				self.room2()
			elif choice == 2:
				self.room4()
			elif choice == 3:
				if self.hasKey:
					print("The door appears to lead to room 1")
					self.doorOpen = True
					self.room1()
			elif choice == 4:
				quit()
			else:
				print("Choose a correct option")

	def room4(self):
		print("Room 4:\nYou see a shiny door at the end of the room")
		while True:
			choice = int(input("Do you:\n1. Move to room 3\n2. Go through the door\n3. Quit\n: "))
			if choice == 1:
				self.room3()
			elif choice == 2:
				print("You completed the game!")
				quit()
			elif choice == 3:
				quit()
			else:
				print("Choose a correct option")


main = Game(input("Name: "))
main.room1()
