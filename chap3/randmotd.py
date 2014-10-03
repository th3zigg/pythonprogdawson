# This program prints a random 'Message of The Day' each time it's run from a choice of 5

import random

msg1 = "Always clean behind your ears"
msg2 = "Loose lips sink ships"
msg3 = "He's not heavy, he's my brother"
msg4 = "If at first you don't succeed, skydiving is not for you"
msg5 = "Do not lean on your own understanding"

random_num = random.randrange(2)

print("Random number:", random_num)

if random_num == 1:
  print(msg1)
elif random_num == 2:
  print(msg2)
elif random_num == 3:
  print(msg3)
elif random_num == 4:
  print(msg4)
elif random_num == 5:
  print(msg5)
