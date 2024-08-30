from util.gen_unique import GenerateUnique as gen

class Department:
    def __init__(self, name, id=gen.generateUniqueId("CADT_IDT")) -> None:
        self.id = id
        self.name = name
        print("id: ", id, name)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name
        }