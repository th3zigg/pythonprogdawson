# This program flips a coin a hundred times and then prints the number of heads and tails

import random


heads = 0
tails = 0
flips = 0

# heads is 1, tails is 2
while flips < 100:
  coin = random.randint(1,2)
  if coin == 1:
    heads += 1
    #print("Heads!")
  else:
    tails += 1
    #print("Tails!")
  flips += 1

print("Coin was flipped", flips, "times")
print("Heads:", heads, "and tails:", tails)
