class Student:
    school = "ABC School"  # class variable

    def __init__(self, name):
        self.name = name  # instance variable

s1 = Student("Alice")
s2 = Student("Bob")

print(s1.school)
print(s2.name)