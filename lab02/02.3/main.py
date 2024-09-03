from student import Student
from services import write_a_student_to_json, read_students_from_json

"""
02.3 Student management
Write a program to allow user to manage a list of student
"""

class Menu:
    def __init__(self) -> None:
        self.students: list(Student) = read_students_from_json()
        # [
        #     Student(1, "Rattanak SETH", 27),
        #     Student(2, "Thearin", 15),
        #     Student(3, "Senghouy", 19)
        # ]


    def create_student(self):
        print("Please input student info:")
        print("Student #%d" %(len(self.students)+1))
        id: int = len(self.students) + 1 #int(input("Student's Id:"))
        name: str = str(input("Student's name:"))
        age: int = int(input("Student's age:"))
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

    def delete_student(self) -> None:
        print("\n==== Delete a student ====")
        while True:
            id = int(input("Input student Id:"))
        
            isDeleted = False
            for idx, stu in enumerate(self.students):
                if (stu.id == id):
                    del self.students[idx]
                    write_a_student_to_json(self.students)
                    print("The following student has been deleted")
                    print("| {:<6} | {:<14} | {:<4} |".format(stu.id, stu.name, stu.age))
                    isDeleted = True
                    break
            if not isDeleted:
                print("Student is not found please try again")
                continue
            else: break
        
            

menu = Menu()

while True:
    print("============ Menu ================")
    print("1. View all students")
    print("2. Add a new student")
    print("3. Delete a students")
    print("4. Quit\n")

    option: int = int(input("Choose an option:"))

    match option:
        case 1:
            menu.student_lists()
            continue
        case 2:
            menu.create_student()
            continue
        case 3:
            menu.delete_student()
            continue
        case 4:
            break
        case _:
            print("Incorrect Input please choose the right one!")
            continue