# Nested Sequence

scores = [("Moe", 1000),("Larry", 1500), ("Curly", 3000)]

print("scores:")
print(scores)

print("\nCurly's Score:")
print(scores[2][1])

name, score = scores[1]

print("\nOther score:")
print(name)
print(score)

print("\n\nName\tScore")
for entry in scores:
  name, score = entry
  print(name, "\t", score)
