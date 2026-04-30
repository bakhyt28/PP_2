students = [("Alice", 23), ("Bob", 19), ("Charlie", 21)]

# сортировка по возрасту
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)