import json
from department import Department

class DepartmentCrud:
    def __init__(self) -> None:
        self.file_path = "data/departments.json"

    def read_department_from_json(self)-> [Department]:
        with open(self.file_path, 'r') as file:
            data = json.load(file)
            deps = [Department(**dep) for dep in data] 
        return deps
    
    def write_to_json(self, data):
        with open(self.file_path, 'w') as file:
            json.dump([dep.to_dict() for dep in data], file, indent=4) 

    