inventory = ("sword","armour","shield","healing potion")

# print each element in the tuple
print("\nYour items:")
for item in inventory:
  print(item)

# get the length of a tuple
print("\nYou have", len(inventory), "items in your possession.")

# test for membership with 'in'
if "sword" in inventory:
  print("\nYou have a sword, you will live to fight another day.")

# display one item through an index
index = int(input("\nEnter the index number ofr an item in inventory: "))
print("At index", index, "is", inventory[index])

# display a slice
print("\n\nDisplaying a tuple slice")
start = int(input("\nEnter the index number to begin a slice: "))
finish = int(input("Enter the index number to end the slice: "))

print("inventory[", start, ":", finish, "] is", end=" ")
print(inventory[start:finish])

input("\n\nPress the enter key to exit.")
