import json
from book import Book

class BookService:
    
    def __init__(self) -> None:
        self.file_path = "data/book.json"

    def read_from_json(self)-> [Book]:
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                students = [Book(**book) for book in data]
            return students
        except:
            return []

    
    def write_to_json(self, books: [Book]):
        with open(self.file_path, 'w') as json_file:
            # file_data = json.load(json_file)
            # file_data.append(student.to_dict())
            json.dump([book.to_dict() for book in books], json_file, 
                                indent=4)
        # with open(self.file_path, 'w') as file:
        #     json.dump([student.to_dict() for student in students], file, indent=4)  # Convert Student objects to dictionaries 
    