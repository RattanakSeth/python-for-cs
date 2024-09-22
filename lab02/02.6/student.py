from department import Department
class Student:
    def __init__(self, id: int, name, age, department) -> None:
        self.id = id
        self.name = name
        self.age = age
        if(isinstance(department, str)): self.department = Department(name=department) # it should ref id like db...
        else: self.department = Department(**department)
        
        print("id: ", id)
        print("department: ", department)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "department": self.department.to_dict()
        }