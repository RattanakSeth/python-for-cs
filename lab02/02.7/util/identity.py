from controller.store import Store
import random 

class Identity:
    def _generateId()-> str:
        store = Store()
        album = store.get_albums()
        id = random.randrange(1,1000)
        while(True):
            is_duplicated: bool = False
            for val in album:
                if val.id == id:
                    id = random.randrange(1,1000)
                    is_duplicated = True
                    break
            if not is_duplicated: break
        return id