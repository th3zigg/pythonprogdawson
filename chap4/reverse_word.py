# This program reverses

word = input("Please enter a word: ")
reversed = ""

for i in range(len(word)-1,-1,-1):
  reversed += word[i]

print("Your word reversed is:", reversed)

input("\n\nPress the enter key to exit.")
