# generators.py

# 1. Generator: squares up to N
def squares_up_to_n(n):
    for i in range(n + 1):
        yield i * i


print("=== Task 1 ===")
for num in squares_up_to_n(5):
    print(num)


# 2. Even numbers from 0 to n (comma separated)
print("\n=== Task 2 ===")
n = int(input("Enter n: "))

even_gen = (str(i) for i in range(n + 1) if i % 2 == 0)
print(",".join(even_gen))


# 3. Numbers divisible by 3 and 4
def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i


print("\n=== Task 3 ===")
for num in divisible_by_3_and_4(50):
    print(num)


# 4. Generator squares from a to b
def squares(a, b):
    for i in range(a, b + 1):
        yield i * i


print("\n=== Task 4 ===")
for num in squares(3, 7):
    print(num)


# 5. Countdown generator from n to 0
def countdown(n):
    while n >= 0:
        yield n
        n -= 1


print("\n=== Task 5 ===")
for num in countdown(5):
    print(num)