from controller.store import Store

class Menu:
    def __init__(self) -> None:
        self.store = Store()

    def view_music_store(self):
        self.store.display_music_album()
    
    def add_song(self):
        print("=========== Create an song ==============")
        title = input("Title:")
        singer = input("Singer:")
        length = input("Length:")
        price = input("Price:")
        albumId = input("AlbumId:")

        self.store.createSong(name=title, singer=singer, length=length, price=price, albumId=albumId)

    def create_an_album(self):
        print("=========== Create an album ==============")
        title = input("Title:")
        self.store.createAlbum(name=title)



menu = Menu()

while True:
    print("============ Menu ================")
    print("1. View a music store")
    print("2. Add a song")
    print("3. Create an album")
    print("4. Quit\n")

    option: int = int(input("Choose an option:"))

    match option:
        case 1:
            menu.view_music_store()
            continue
        case 2:
            menu.add_song()
            continue
        case 3:
            menu.create_an_album()
            continue
        case 4:
            break
        case _:
            print("Incorrect Input please choose the right one!")
            continue