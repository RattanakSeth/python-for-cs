# from .song import Song
# from .album import Album
from model import Album, Song
from itertools import groupby
from operator import attrgetter

class Store:
   
    def __init__(self) -> None:
        self.songs = []
        self.albums = []

    #TODO: populate or expand inside ref object
    def display_music_album(self):
        print("======= Music Store ========")
        # for song in self.songs:
        # Group students by id
        grouped_songs = {key: list(group) for key, group in groupby(self.songs, key=attrgetter('album'))}

        # Print the grouped students
        for album, group in grouped_songs.items():
            print(f"ID {album}: {group}")


    def createSong(self, name, singer, length, price, albumId: int)-> bool:
        if (not albumId):
            print("400: AlbumId is required")
            return False
        self.songs.append(Song(name, singer, length, price, albumId))
        print("Song is created")
        return True
    
    def createAlbum(self, name)-> bool:
        
        self.albums.append(Album(name=name, id=len(self.albums)+1))
        print("Album is created")
        return True

    def get_albums(self)-> list:
        return self.albums