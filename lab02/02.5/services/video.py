import json
from video import Video

class VideoService:
    
    def __init__(self) -> None:
        self.file_path = "data/video.json"

    def read_from_json(self)-> [Video]:
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                students = [Video(**v) for v in data]
            return students
        except:
            return []

    
    def write_to_json(self, videos: [Video]):
        with open(self.file_path, 'w') as json_file:
            # file_data = json.load(json_file)
            # file_data.append(student.to_dict())
            json.dump([v.to_dict() for v in videos], json_file, indent=4)
        # with open(self.file_path, 'w') as file:
        #     json.dump([student.to_dict() for student in students], file, indent=4)  # Convert Student objects to dictionaries 
    