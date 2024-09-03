class Student:
    def __init__(self, id: int, name: str, age: int) -> None:
        self.id = id
        self.name = name
        self.age = age
    
    def get_name(self):
        return self.name
    
    def setValues(self, id, name, age) -> None:
        self.id = id
        self.name = name
        self.age = age

    def display(self):
        print("| {:<6} | {:<14} | {:<4} |".format(self.id, self.name, self.age))

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age
        }
