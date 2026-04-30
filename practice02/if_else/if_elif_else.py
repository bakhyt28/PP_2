a = 200
b = 33
if b > a: # Initial conditional check: evaluates if 'b' exceeds 'a'
  print("b is greater than a")
elif a == b: # Secondary check: only runs if the first condition was False
  print("a and b are equal")
else: # Fallback: executes if all preceding conditions are False
  print("a is greater than b")