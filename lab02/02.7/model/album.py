class Album:
    def __init__(self, name, id: int) -> None:
        self.id = id
        self.name = name

    def to_dict(self)-> dict:
        return {
            "id": self.id,
            "name": self.name
        }
