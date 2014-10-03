# Guess My Number

import random

print("\nWelcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100")
print("You get 5 attempts at guessing.\n")

# set the initial values
the_number = random.randint(1, 100)
guess = int(input("Take a guess: "))
tries = 1

# guessing loop
while guess != the_number and tries < 5:
  if guess > the_number:
    print("Lower ...")
  else:
    print("Higher ...")


  guess = int(input("Take a guess: "))
  tries += 1

if guess != the_number:
  print("Sorry, you didn't guess the number in", tries, "tries. Game over!")
else:
  print("You guessed it!  The number was", the_number)
  print("And it only took you", tries, "tries!\n")

input("\n\nPress the enter key to exit")
