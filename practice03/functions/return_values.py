def square(x):
    return x * x

print(square(4))

# Возврат нескольких значений
def get_user():
    return "John", 25

name, age = get_user()
print(name, age)