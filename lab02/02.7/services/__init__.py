from .album import AlbumService
from .song import SongService

albumService = AlbumService()
songService = SongService()

__all__ = ["albumService", "songService"]
