import json
from student import Student

class StudentService:
    
    def __init__(self) -> None:
        self.file_path = "data/students.json"

    def read_students_from_json(self)-> [Student]:
        with open(self.file_path, 'r') as file:
            data = json.load(file)
            students = [Student(**student) for student in data]  # Create Student objects from the data
        return students
    
    def write_a_students_to_json(self, students: [Student]):
        with open(self.file_path, 'w') as json_file:
            # file_data = json.load(json_file)
            # file_data.append(student.to_dict())
            json.dump([student.to_dict() for student in students], json_file, 
                                indent=4)
        # with open(self.file_path, 'w') as file:
        #     json.dump([student.to_dict() for student in students], file, indent=4)  # Convert Student objects to dictionaries 
    