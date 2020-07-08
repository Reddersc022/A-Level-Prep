import tkinter
from Encoding_Functions import *

root = tkinter.Tk()
root.title = "Ciphering"

# Top rows

l1 = tkinter.Label(root, text="Plaintext File Name:")
l1.grid(column=0, row=0, pady=5)

e1 = tkinter.Entry(root)
e1.grid(column=0, row=1, padx=10)

l1 = tkinter.Label(root, text="Ciphertext File Name:")
l1.grid(column=1, row=0, pady=5)

e2 = tkinter.Entry(root)
e2.grid(column=1, row=1, padx=10)

l2 = tkinter.Label(root, text="Encoding Type:")
l2.grid(column=0, row=2, pady=10)

# Buttons

b1 = tkinter.Button(root, text="Caesar", command=lambda: caesar(e1.get(), e2.get()))
b1.grid(column=0, row=3, padx=10)

b2 = tkinter.Button(root, text="Vigenere", command=lambda: vigenere(e1.get(), e2.get()))
b2.grid(column=1, row=3, padx=10)

pad1 = tkinter.Label(root, text='')
pad1.grid(column=0, row=4, columnspan=2)

b3 = tkinter.Button(root, text="Bacon", command=lambda: bacon(e1.get(), e2.get()))
b3.grid(column=0, row=5, padx=10)

b4 = tkinter.Button(root, text="Morse", command=lambda: morse(e1.get(), e2.get()))
b4.grid(column=1, row=5, padx=10)

pad2 = tkinter.Label(root, text='')
pad2.grid(column=0, row=6, columnspan=2)

tkinter.mainloop()
