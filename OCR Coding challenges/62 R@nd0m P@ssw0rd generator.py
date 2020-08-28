from english_words import english_words_set  # I changed it to a list so I can use it
import random

print("R@nd0m P@ssw0rd generator")

# NCSC recommends a password of 3 random words

print(random.choice(english_words_set).title()
	+ random.choice(english_words_set).title()
	+ random.choice(english_words_set).title())
