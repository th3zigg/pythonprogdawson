# Geek translator
# Demonstrates using dictionaries

geek = {"404": "Clueless",
        "Googling": "Searching the Internet",
        "Keyboard plaque": "collection of debris found in a computer keyboard",
        "Percussive Maintence": "the act of striking an electronic device to make it work",
        "Uninstalled": "Fired"}


print(geek["404"])

if "400" not in geek:
  print("No bad requests here")
else:
  print("Found a bad request")

print(geek.get("Keboard plaque", "Hamna!"))

print("Geek terms: ", geek.keys())
