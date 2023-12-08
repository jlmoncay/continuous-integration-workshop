from datetime import datetime, timedelta

class Book:
    def __init__(self, title, author, available_quantity):
        self.title = title
        self.author = author
        self.available_quantity = available_quantity

class Library:
    def __init__(self):
        self.books = [
            Book("Book1", "Author1", 5),
            Book("Book2", "Author2", 10),
            # Agrega más libros según sea necesario
        ]
        self.checked_out_books = []

    def checkout_books(self):
        print("Checkout Books:")
        self.display_catalog()

        selected_books = []
        total_quantity = 0

        while True:
            book_title = input("Enter the title of the book you want to checkout (or 'done' to finish): ")

            if book_title.lower() == 'done':
                break

            book = next((b for b in self.books if b.title == book_title), None)

            if book:
                quantity = self.validate_quantity(input(f"Enter the quantity for '{book.title}': "))
                if quantity == -1:
                    continue

                if total_quantity + quantity > 10:
                    print("Error: Maximum 10 books allowed per checkout. Please adjust your selection.")
                    continue

                if quantity > book.available_quantity:
                    print(f"Error: Insufficient quantity of '{book.title}' available.")
                    continue

                selected_books.append({"book": book, "quantity": quantity})
                total_quantity += quantity
                book.available_quantity -= quantity

                print(f"'{book.title}' added to your checkout.")

            else:
                print(f"Error: Book '{book_title}' not found in the catalog.")

        if selected_books:
            self.display_checkout_summary(selected_books)
        else:
            print("Checkout process canceled.")

    def display_catalog(self):
        print("Library Catalog:")
        for book in self.books:
            print(f"{book.title} by {book.author} - Available: {book.available_quantity}")

    def validate_quantity(self, quantity):
        try:
            quantity = int(quantity)
            if quantity > 0:
                return quantity
            else:
                raise ValueError("Please enter a positive integer greater than zero.")
        except ValueError as e:
            print(f"Error: {e}")
            return -1

    def calculate_due_date(self):
        return datetime.now() + timedelta(days=14)

    def calculate_late_fee(self, due_date):
        current_date = datetime.now()
        if current_date > due_date:
            days_late = (current_date - due_date).days
            return days_late * 1  # $1 per day late fee
        else:
            return 0

    def return_books(self):
        print("Return Books:")
        self.display_checked_out_books()

        user_returned_books = []
        while True:
            book_title = input("Enter the title of the book you want to return (or 'done' to finish): ")

            if book_title.lower() == 'done':
                break

            # Asegura que la búsqueda sea insensible a mayúsculas y minúsculas
            book_title_lower = book_title.lower()
            checked_out_book = next((b for b in self.checked_out_books if b["book"].title.lower() == book_title_lower), None)

            if checked_out_book:
                returned_quantity = self.validate_quantity(input(f"Enter the quantity of '{book_title}' being returned: "))
                if returned_quantity == -1:
                    continue

                if returned_quantity <= checked_out_book["quantity"]:
                    checked_out_book["quantity"] -= returned_quantity
                    book = checked_out_book["book"]
                    book.available_quantity += returned_quantity

                    if checked_out_book["quantity"] == 0:
                        self.checked_out_books.remove(checked_out_book)

                    print(f"{returned_quantity}x '{book.title}' returned successfully.")
                    user_returned_books.append({"book": book, "quantity": returned_quantity})

                else:
                    print("Error: Invalid quantity for return. Please enter a valid quantity.")

            else:
                print(f"Error: Book '{book_title}' not found in the checked-out books.")

        if user_returned_books:
            self.display_return_summary(user_returned_books)
        else:
            print("Return process canceled.")

    def display_checked_out_books(self):
        print("Checked-out Books:")
        for checked_out_book in self.checked_out_books:
            book = checked_out_book["book"]
            quantity = checked_out_book["quantity"]
            print(f"{quantity}x '{book.title}'")

    def display_checkout_summary(self, selected_books):
        print("\nCheckout Summary:")
        for item in selected_books:
            book = item["book"]
            quantity = item["quantity"]
            due_date = self.calculate_due_date()
            print(f"{quantity}x '{book.title}' due on {due_date.strftime('%Y-%m-%d')}")

    def display_return_summary(self, returned_books):
        print("\nReturn Summary:")
        total_late_fee = 0
        for item in returned_books:
            book = item["book"]
            returned_quantity = item["quantity"]
            due_date = self.calculate_due_date()
            late_fee = self.calculate_late_fee(due_date)
            total_late_fee += late_fee
            print(f"{returned_quantity}x '{book.title}' returned. Late fee: ${late_fee}")

        print(f"Total late fees incurred: ${total_late_fee}")

# Ejemplo de uso básico
library = Library()

while True:
    print("\n1. Display Catalog\n2. Checkout Books\n3. Return Books\n4. Exit")
    choice = input("Select an option: ")

    if choice == '1':
        library.display_catalog()
    elif choice == '2':
        library.checkout_books()
    elif choice == '3':
        library.return_books()
    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
