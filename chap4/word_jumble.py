# Word Jumble
#
# The computer picks a random word and then "jumbles" it
# The player has to guess the original word

import random

# create a sequence of words to choose from
WORDS = ("python", "jumble", "easy", "difficult", " answer", "xylophone")

# pick one word randomly from the sequence
word = random.choice(WORDS)

# create a variable to use late to see if the guess is correct
correct = word

# create a jumbled version of the word
jumble = ""

while word:
  position = random.randrange(len(word))
  jumble += word[position]
  word = word[:position] + word[(position + 1):]

# start the game
print(
"""

          Welcome to Word Jumble!

    Unscramble the letters to make a word.
(Press the enter key at the prompt to quit.)
"""
)

print("The jumble is:", jumble)
