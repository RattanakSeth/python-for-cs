from student import Student
from services.student_crud import StudentCrud

class Menu:
    def __init__(self) -> None:
        self.studentService = StudentCrud()
        self.students: list(Student) = self.studentService.read_students_from_json()
    
    # create and write it to json file
    def create_student(self):
        print("Please input student info:")
        print("Student #%d" %(len(self.students)+1))
        id: int = int(input("Student's Id:"))
        name: str = str(input("Student's name:"))
        age: int = int(input("Student's age:"))
        department = input("Department:")
        student = Student(id, name, age, department)
        self.students.append(student)
        self.studentService.write_students_to_json(self.students)
        print("A student is added to the list\n")

    def student_lists(self):
        print("\n======================================================")
        print("| No  | ID     | Name           | Age  | Department     |")
        print("======================================================")
        for idx, student in enumerate(self.students):
            print("| {:<3} | {:<6} | {:<14} | {:<4} | {:<17}".format(idx+1, student.id, student.name, student.age, student.department.name))
        print("======================================================\n")

    
    def delete_student(self) -> None:
        print("\n==== Delete a student ====")
        while True:
            id = int(input("Input student Id:"))
        
            isDeleted = False
            for idx, stu in enumerate(self.students):
                if (stu.id == id):
                    del self.students[idx]
                    self.studentService.write_students_to_json(self.students)
                    # should remove from json as well
                    print("The following student has been deleted")
                    print("| {:<6} | {:<14} | {:<4} |".format(stu.id, stu.name, stu.age, stu.department))
                    isDeleted = True
                    break
            if not isDeleted:
                print("Student is not found please try again")
                continue
            else: break

    def view_departments(self):
        print("Department will use inside department due ot json format")


menu = Menu()

while True:
    print("============ Menu ================")
    print("1. View all students")
    print("2. Add a new student")
    print("3. Delete a students")
    print("4. Add Department")
    print("5. View Departments")
    print("6. Quit\n")

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
            print("Please use existing data input, System do not allow to input dep..\n")
            print("TODO next for data ref")
            continue
        case 5:
            menu.view_departments()
            continue
        case 6:
            break
        case _:
            print("Incorrect Input please choose the right one!")
            continue