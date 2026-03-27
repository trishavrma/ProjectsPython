class Book:
    def __init__(self, title):
        self.title = title
        self.available = True


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed = []


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self):
        title = input("Enter book title: ")
        self.books.append(Book(title))
        print("Book added")

    def add_member(self):
        name = input("Enter member name: ")
        self.members.append(Member(name))
        print("Member added")

    def lend_book(self):
        name = input("Enter member name: ")
        title = input("Enter book title: ")

        for m in self.members:
            if m.name == name:
                for b in self.books:
                    if b.title == title and b.available:
                        b.available = False
                        m.borrowed.append(title)
                        print("Book issued")
                        return
        print("Book not available")

    def return_book(self):
        name = input("Enter member name: ")
        title = input("Enter book title: ")

        for m in self.members:
            if m.name == name and title in m.borrowed:
                for b in self.books:
                    if b.title == title:
                        b.available = True
                        m.borrowed.remove(title)
                        print("Book returned")
                        return
        print("Invalid return")

    def display_books(self):
        print("\nBooks List:")
        for b in self.books:
            print(b.title, "-", "Available" if b.available else "Issued")


lib = Library()

while True:
    print("\n1.Add Book  2.Add Member  3.Lend Book  4.Return Book  5.Display Books  6.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        lib.add_book()
    elif ch == 2:
        lib.add_member()
    elif ch == 3:
        lib.lend_book()
    elif ch == 4:
        lib.return_book()
    elif ch == 5:
        lib.display_books()
    elif ch == 6:
        break
    else:
        print("Invalid choice")