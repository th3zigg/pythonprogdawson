# Hero's Inventory
# Demonstrates tuple creation

# create an empty tuple
inventory = ("sword","armour","shield","healing potion")

# treat the tuple as a condition
if not inventory:
  print("You are empty handed.")
else:
  print("\nThe tuple inventory is:")
  print(inventory)

# print each element in the tuple
print("\nYour items:")
for item in inventory:
  print(item)

input("\n\nPress the enter key to exit.")
