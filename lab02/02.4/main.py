from book import Book

class Menu:
    def __init__(self) -> None:
        self.books: list(Book) = [
            Book(
                ISBN="0671027034",
                title="How to Win Friends & Influence People",
                price=10.29,
                author="Dale Carnegie"
            ),
            Book(
                ISBN="0743273567",
                title="The Great Gatsby",
                price=15.99,
                author="F. Scott Fitzgerald"
            ),
            Book(
                ISBN="0451524934",
                title="1984",
                price=9.99,
                author="George Orwell"
            ),
            Book(
                ISBN="0316769487",
                title="The Catcher in the Rye",
                price=12.49,
                author="J.D. Salinger"
            ),
            Book(
                ISBN="0061120081",
                title="To Kill a Mockingbird",
                price=14.99,
                author="Harper Lee"
            )
        ]


    def book_lists(self):
        print("\n======================================================================")
        print("| No  | ISBN        | Title                             | Price   | Author         |")
        print("======================================================================")
        for idx, book in enumerate(self.books):
            print("| {:<3} | {:<10} | {:<32} | {:<7.2f} | {:<14} |".format(idx+1, book.ISBN, book.title, book.price, book.author))
        print("======================================================================\n")


    def create_book(self):
        print("========= Add a new book ===========")
        print("Student #%d" %(len(self.books)+1))
        ISBN: str = str(input("ISBN:"))
        title: str = str(input("Title:"))
        price: int = int(input("Price:"))
        author: int = str(input("Author:"))
        self.books.append(Book(ISBN, title, price, author))
        print("A book is added to the list\n")

    def update_book(self):
        while True:
            isbn = input("Input ISBN:")
            # isFound: bool = False
            isUpdated: bool = False
            for idx, book in enumerate(self.books):
                if book.ISBN == isbn:
                    print("Please update the following:\n")
                    self.books[idx].display()
                    ISBN: str = input(f"ISBN [{book.ISBN}]: ") or book.ISBN
                    title: str = input(f"Title [{book.title}]: ") or book.title
                    price: int = int(input(f"Price [{book.price}]: ") or book.price)
                    author: str = input(f"Author [{book.author}]: ") or book.author

                    self.books[idx].set(ISBN, title, price, author)
                    isUpdated = True
                    print("Book has been updated successfully")
                    break

            if (not isUpdated):
                print("Book is not found. Try again")
                continue
            else: break
                    # self.books[idx]


menu = Menu()

while True:
    print("============ Menu ================")
    print("1. View all books")
    print("2. Add a new book")
    print("3. update a book")
    print("4. Quit\n")

    option: int = int(input("Choose an option:"))

    match option:
        case 1:
            menu.book_lists()
            continue
        case 2:
            menu.create_book()
            continue
        case 3:
            menu.update_book()
            continue
        case 4:
            break
        case _:
            print("Incorrect Input please choose the right one!")
            continue