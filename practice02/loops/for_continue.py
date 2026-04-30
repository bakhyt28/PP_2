fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana": #If "banana" is encountered, skip the rest of this iteration.
    continue
  print(x) # This line is only reached for "apple" and "cherry".