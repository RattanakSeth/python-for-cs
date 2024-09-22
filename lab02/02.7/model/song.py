class Song:
    def __init__(self, name, singer, length, price, albumId: int) -> None:
        self.name = name
        self.singer = singer
        self.length = length
        self.price = price
        self.album = albumId

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "singer": self.singer,
            "length": self.length,
            "price": self.price,
            "album": self.album
        }