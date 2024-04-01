from datetime import datetime, timedelta

library = {
    1: {"title": "Atomic Habits", "author": "James Clear", "quantity": 5},
    2: {"title": "Zero to One", "author": "Peter Theil", "quantity": 3},
    3: {"title": "Steal like an Artist", "author": "Austin Kleon", "quantity": 7},
}

userbase = {}

transactions = []

def display_library():
    print("Library:")
    for book_id, book_info in library.items():
        available_status = "Available" if book_info['quantity'] > 0 else "Not Available"
        print(f"{book_id}. {book_info['title']} by {book_info['author']} - {book_info['quantity']} books {available_status} ")

def user_registration():
    user_id = input("Enter your unique user ID : ")
    user_name = input("Enter your name : ")
    userbase[user_id] = {'name': user_name, 'books_checked_out': {}}

def book_checkout():
    user_id = input("Enter your user ID: ")
    if user_id not in userbase:
        print("You are not registered as a user. Please register first.")
        return

    book_id = int(input("Please enter the book ID you wish to check out: "))
    if book_id not in library or library[book_id]['quantity'] == 0:
        print("The book is currently unavailable for checkout.")
        return

    if len(userbase[user_id]['books_checked_out']) >= 3:
        print("You've reached the maximum limit for checked-out books (3).")
        return

    checkout_date = datetime.now().strftime("%Y-%m-%d")
    due_date = (datetime.now() + timedelta(days=14)).strftime("%Y-%m-%d")

    transactions.append({'user_id': user_id, 'book_id': book_id, 'checkout_date': checkout_date, 'due_date': due_date})
    userbase[user_id]['books_checked_out'][book_id] = due_date
    library[book_id]['quantity'] -= 1
    print("The book has been successfully checked out.")

def return_book():
    user_id = input("Enter your user ID: ")
    if user_id not in userbase:
        print("You are not registered as a user. Please register first.")
        return

    book_id = int(input("Please enter the book ID you wish to return:"))
    if book_id not in library:
        print("Invalid book ID.")
        return

    if book_id not in userbase[user_id]['books_checked_out']:
        print("You haven't checked out this book.")
        return

    return_date = datetime.now().strftime("%Y-%m-%d")
    due_date = datetime.strptime(userbase[user_id]['books_checked_out'][book_id], "%Y-%m-%d")
    
    days_overdue = max(0, (datetime.now() - due_date).days)
    fine = days_overdue * 1  # $1 per day overdue

    library[book_id]['quantity'] += 1
    del userbase[user_id]['books_checked_out'][book_id]

    print("Book returned successfully.")
    if days_overdue > 0:
        print(f"Overdue fine: ${fine}")

def display_overdue_books():
    user_id = input("Enter your user ID: ")
    if user_id not in userbase:
        print("You are not registered as a user. Please register first.")
        return

    overdue_books = []
    total_fine = 0

    for transaction in transactions:
        if transaction['user_id'] == user_id:
            due_date = datetime.strptime(transaction['due_date'], "%Y-%m-%d")
            if due_date < datetime.now():
                days_overdue = (datetime.now() - due_date).days
                fine = days_overdue * 1
                total_fine += fine
                overdue_books.append((transaction['book_id'], days_overdue, fine))

    if not overdue_books:
        print("No overdue books.")
    else:
        print("Overdue Books:")
        for book_id, days_overdue, fine in overdue_books:
            print(f"Book ID {book_id}: Overdue by {days_overdue} days. Fine is: ${fine}")
        print(f"Total Fine: ${total_fine}")

def display_menu():
    print("\nMenu:")
    print("1. Display Library")
    print("2. User Registation")
    print("3. Book Checkout")
    print("4. Return Book")
    print("5. Display Overdue Books and Fines")
    print("6. Exit")

def main():
    while True:
        display_menu()
        choice = input("Please enter your choice (1-6): ")

        if choice == '1':
            display_library()
        elif choice == '2':
            user_registration()
        elif choice == '3':
            book_checkout()
        elif choice == '4':
            return_book()
        elif choice == '5':
            display_overdue_books()
        elif choice == '6':
            print("You are now exiting the Library Management System. Sayonara!")
            break
        else:
            print("Your choice is invalid. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
