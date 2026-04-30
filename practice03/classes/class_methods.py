class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hi, I'm", self.name)

p = Person("Bob")
p.greet()