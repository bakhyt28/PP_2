# *args
def sum_all(*numbers):
    return sum(numbers)

print(sum_all(1, 2, 3, 4))

# **kwargs
def print_info(**data):
    for key, value in data.items():
        print(key, ":", value)

print_info(name="Alice", age=22)