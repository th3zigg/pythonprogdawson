# assign by index
inventory = ["sword","armor", "shield", "healing potion","gold", "gems"]
print("Your current inventory: ", inventory)

print("\nYou trade your sword for a crossbow.")
inventory[0] = "crossbow"
print("Your inventory is now: ", inventory)

# assign by slice
print("\nYou use your gold and gems to buy an orb of future telling.")
inventory[4:6] = ["orb of future telling"]

# delete an element
print("\nIn a great battle, your shield is destroyed.")
del inventory[2]
print("Your inventory is now: ", inventory)

# delete a slice
print("\nYour crossbow and armor are stolen by thieves.")
del inventory[:2]
print("Your inventory is now: ", inventory)
