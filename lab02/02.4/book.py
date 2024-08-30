class Book:
    def __init__(self, ISBN, title, price: int, author) -> None:
        self.ISBN = ISBN
        self.title = title
        self.price = price
        self.author = author

    def set(self, ISBN, title, price, author):
        if ISBN: 
            self.ISBN = ISBN
            # print("Attribute set: ", ISBN)
        if title: self.title = title
        if price: self.price = price
        if author: self.author = author

    def display(self):
        print("\n======================================================================")
        print("| No  | ISBN        | Title                             | Price   | Author         |")
        print("======================================================================")
        print("| {:<3} | {:<10} | {:<32} | {:<7.2f} | {:<14} |".format(1, self.ISBN, self.title, self.price, self.author))
        print("======================================================================\n")

        