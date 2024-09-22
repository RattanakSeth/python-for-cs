import json
from model import Album

class AlbumService:
    def __init__(self) -> None:
        self.file_path = "data/albums.json"

    def read_from_json(self)-> [Album]:
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                print(data)
                albums = [Album(**album) for album in data] 
                file.close()
            return albums
        except NameError:
            print("error in load album: ", NameError)
            return []
    
    def write_to_json(self, data):
        with open(self.file_path, 'w') as file:
            json.dump([d.to_dict() for d in data], file, indent=4) 
            file.close()

    