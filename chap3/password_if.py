# Password
# Demonstrates the if statement

print("Welcome to System Security Inc.")

print("-- where security is our middle name\n")

password = input("Enter your password: ")

if password == "secret":
  print("Access Granted")
elif password == "asdfdf":
  print("Access Denied, try harder")
else:
  print("Sorry, no entry")


input("\n\nPress the enter key to exit")
