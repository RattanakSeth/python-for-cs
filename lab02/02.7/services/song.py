import json
from model import Song

class SongService:
    def __init__(self) -> None:
        self.file_path = "data/song.json"

    def read_from_json(self)-> [Song]:
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                # print("dat: ", [{**song, 'albumId': song.pop('album')} for song in data])
                # songs = [Song(**{**song, 'albumId': song.pop('album')}) for song in data]
                songs = [Song(**{key: value for key, value in song.items() if key != 'album'}, albumId=song['album']) for song in data]
            return songs
        except NameError:
            print("Error in load song: ", NameError)
            return []
    
    def write_to_json(self, songs):
        with open(self.file_path, 'w') as file:
            json.dump([s.to_dict() for s in songs], file, indent=4)

    