# Позиционные аргументы
def introduce(name, age):
    print(f"My name is {name}, I am {age} years old")

introduce("Bob", 20)

# Значения по умолчанию
def greet(name="Guest"):
    print("Hello,", name)

greet()
greet("Anna")