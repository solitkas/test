from collections import defaultdict

data = [
    ("sasa", 2),
    ("peta", 2),
    ("peta", 1),
    ("sasa", 3),
    ("sasa", 3),
    ("natasha", 4),

]

marks = defaultdict(list)
for name, mark in data:
    marks[name].append(mark)

print(marks)






