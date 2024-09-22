# from .song import Song
# from .album import Album
from model import Album, Song
from itertools import groupby
from operator import attrgetter
from services import albumService, songService

class Store:
   
    def __init__(self) -> None:
        self.songs = songService.read_from_json()
        self.albums = albumService.read_from_json()

    def findAlbumById(self, id):
        for idx, album in enumerate(self.albums):
           if (album.to_dict()['id'] == id):
               return album
        return None
         
    def display_music_album(self):
        print("\n======= Music Store ========")
        # Group students by id
        grouped_songs = {key: list(group) for key, group in groupby(self.songs, key=attrgetter('album'))}

        # Print the grouped students
        for album, group in grouped_songs.items():
            findAlbum = self.findAlbumById(int(album))
            # albums = albumById.get(1)
            # print(albumById, albums)
            
            print(f"Album {album}: {findAlbum.name if findAlbum else "NO Field"}")
            for idx, song in enumerate(group):
                print("| {:<3} | {:<6} | {:<14} | {:<4} | {:<17}".format(idx+1, song.name, song.singer, song.length, song.price))

        print("\n")


    def createSong(self, name, singer, length, price, albumId: int)-> bool:
        if (not albumId):
            print("400: AlbumId is required")
            return False
        self.songs.append(Song(name, singer, length, price, albumId))
        songService.write_to_json(self.songs)
        print("Song is created")
        return True
    
    def createAlbum(self, name)-> bool:
        print("ID#%d" % (len(self.albums)+ 1))
        self.albums.append(Album(name=name, id=len(self.albums)+1))
        albumService.write_to_json(self.albums)
        print("Album is created")
        return True

    def get_albums(self)-> list:
        return self.albums