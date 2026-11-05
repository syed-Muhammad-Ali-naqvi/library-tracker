books = {} 

def show_menu():
    print("\n=== Library Tracker ===")
    print("1. Add book")
    print("2. List books")
    print("0. Exit")


def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "0":
            print("Goodbye!")
            break
        elif choice == "2":
            list_books()
        elif choice == "1":
            add_book()
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()

def list_books():
    if not books:
        print("No books in the library.")
        return

    for title, details in books.items():
        status = "Available" if details["available"] else "Borrowed"
        print(f'{title} by {details["author"]} - {status}')
def add_book():
    title = input("Title: ").strip()
    author = input("Author: ").strip()

    if title in books:
        print(f'"{title}" is already in the library.')
    else:
        books[title] = {
            "author": author,
            "available": True
        }
        print(f'Added "{title}".')

