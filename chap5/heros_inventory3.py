# Hero's Inventory 3.0
# Demonstrates lists

# create a list with some items and display with a for loop
inventory = ["sword","armor", "shield", "healing potion"]

print("You have", len(inventory), "items in your possession")
print("\nYour items:")
for item in inventory:
  print(item)

index = int(input("\nEnter the index number for an item in inventory: "))
print("At index", index, "is", inventory[index])

print("\nDisplaying a slice")
start = int(input("\nEnter the index number to begin a slice: "))
finish = int(input("Enter the index number to end the slice: "))
print("inventory[", start, ":", finish, "] is", end=" ")
print(inventory[start:finish])

input("\nPress the enter key to continue")
