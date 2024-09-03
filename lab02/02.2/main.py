"""
02.2 Infinite Input of Student
Write a program in Java to manage student by using Student Class:
    - Attributes (id, name, age, etc.)
    - Must implement the following methods in Student class:
    - setValues()
    - display()
"""

from student import Student
from services import write_a_student_to_json, read_students_from_json

class Menu:
    def __init__(self) -> None:
        self.students: list(Student) = read_students_from_json()


    def create_student(self):
        print("Please input student info:")
        print("Student #%d" %(len(self.students)+1))
        id: int = int(input("Student's Id:"))
        name: str = str(input("Student's name:"))
        age: int = int(input("Student's age:"))
        # student = Student(id, name, age)
        self.students.append(Student(id, name, age))
        write_a_student_to_json(self.students)
        print("A student is added to the list\n")

    def student_lists(self):
        print("\n======================================================")
        print("| No  | ID     | Name           | Age  |")
        print("======================================================")
        for idx, student in enumerate(self.students):
            print("| {:<3} | {:<6} | {:<14} | {:<4} |".format(idx+1, student.id, student.name, student.age))
        print("======================================================\n")

menu = Menu()
while True:
    print("============ Menu ================")
    print("1. Create a student")
    print("2. List students")
    print("3. Quit\n")

    option: int = int(input("Choose an option:"))

    match option:
        case 1:
            menu.create_student()
            continue
        case 2:
            menu.student_lists()
            continue
        case 3:
            exit()
            break
        case _:
            print("Incorrect Input please choose the right one!")
            continue
