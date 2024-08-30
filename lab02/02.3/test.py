from student import Student

s1 = Student(1, "Rattanak", age=27)
s2 = Student(2, "Ravae", age=27)

stuList: list = [s1, s2]

matches = matches = [True if x.id == 3 else False for x in stuList]
print(matches.pop())