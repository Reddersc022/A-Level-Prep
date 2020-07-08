import tkinter
from tkinter import messagebox


def fileCheck(plaintext: str, filename: str) -> bool:
	try:
		open(plaintext, 'r')
		open(filename, 'r')
		return True

	except FileNotFoundError:
		messagebox.showerror(title="Error", message="File does not exist")
		return False


def caesar(plaintext: str, filename: str) -> None:
	# Does not maintain caps or punctuation but works nonetheless
	if not fileCheck(plaintext, filename):
		return

	with open(plaintext, "r") as f:
		text = f.read()

	window = tkinter.Tk()
	window.title = "Caesar"

	l1 = tkinter.Label(window, text="Shift:")
	l1.grid(column=0, row=0)

	e1 = tkinter.Entry(window)
	e1.grid(column=0, row=1)

	def go():
		messagebox.showinfo(title="Result", message="Encoded Text: %s" % ''.join(map(chr,
			[ord(i) + int(e1.get()) + (6 if 90 < ord(i) + int(e1.get()) < 97 else 0) for i in text])).upper())

	b1 = tkinter.Button(window, text="Confirm", command=go)
	b1.grid(column=0, row=2)


def vigenere(plaintext: str, filename: str) -> None:
	# Does not end up with latin-alphabetic letters, keep punctuation, or maintain caps but works nonetheless
	if not fileCheck(plaintext, filename):
		return

	with open(plaintext, "r") as f:
		text = f.read()

	window = tkinter.Tk()
	window.title = "Vigenere"

	l1 = tkinter.Label(window, text="Keyword:")
	l1.grid(column=0, row=0)

	e1 = tkinter.Entry(window)
	e1.grid(column=0, row=1)

	def go():
		keyword = (e1.get() * ((len(text) // len(e1.get())) + 1))[:len(text)]
		messagebox.showinfo(title="Result", message="Encoded Text: %s" % ''.join(map(chr, [ord(i) + ord(j) +
																						   (6 if 90 < ord(i) + ord(
																							   j) < 97 else 0) for i, j
			in zip(text, keyword)])).upper())

	b1 = tkinter.Button(window, text="Confirm", command=go)
	b1.grid(column=0, row=2)


def bacon(plaintext: str, filename: str) -> None:
	if not fileCheck(plaintext, filename):
		return

	with open(plaintext, "r") as f:
		text = f.read()

	text = "hello"

	reference = {'A': 'aaaaa', 'B': 'aaaab', 'C': 'aaaba', 'D': 'aaabb', 'E': 'aabaa', 'F': 'aabab', 'G': 'aabba',
		'H': 'aabbb', 'I': 'abaaa', 'J': 'abaab', 'K': 'ababa', 'L': 'ababb', 'M': 'abbaa', 'N': 'abbab', 'O': 'abbba',
		'P': 'abbbb', 'Q': 'baaaa', 'R': 'baaab', 'S': 'baaba', 'T': 'baabb', 'U': 'babaa', 'V': 'babab', 'W': 'babba',
		'X': 'babbb', 'Y': 'bbaaa', 'Z': 'bbaab'}  # Single quotes because it was a pain to do

	window = tkinter.Tk()
	window.title = "Bacon"

	def go():
		messagebox.showinfo(title="Result",
			message="Encoded Text: %s" % ' '.join(list(map(lambda x: reference[x], text.upper()))))

	b1 = tkinter.Button(window, text="Confirm", command=go)
	b1.grid(column=0, row=2)


def morse(plaintext: str, filename: str) -> None:
	if not fileCheck(plaintext, filename):
		return

	with open(plaintext, "r") as f:
		text = f.read()

	reference = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
		'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-',
		'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..'}
	# Single quotes because it was a pain to do

	window = tkinter.Tk()
	window.title = "Bacon"

	def go():
		messagebox.showinfo(title="Result",
			message="Encoded Text: %s" % ' '.join(list(map(lambda x: reference[x], text.upper()))))

	b1 = tkinter.Button(window, text="Confirm", command=go)
	b1.grid(column=0, row=2)
