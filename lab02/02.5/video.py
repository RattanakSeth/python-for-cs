class Video:
    def __init__(self, title, singer, uploader, length, type) -> None:
        self.title = title
        self.singer = singer
        self.uploader = uploader
        self.length = length
        self.type = type

    def to_dict(self):
        return {
            "title": self.title,
            "singer": self.singer,
            "uploader": self.uploader,
            "length": self.length,
            "type": self.type
        }