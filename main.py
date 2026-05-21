from datetime import date
from book import Book
from member import Member
from loan import Loan
from exception import BookUnavailableError

def main():
    book1 = Book("B001", "Clean Code", "Robert Martin", "978-123", 2008)
    member1 = Member("M001", "Alice", "alice@email.com", "555-1234")
    member2 = Member("M002", "Bob", "bob@email.com", "555-6789")

    try:        
        print(f"Attempting to borrow '{book1.title}' for Alice...")
        loan1 = Loan("L001", book1, member1, date.today())
        print("Loan 1 created successfully!")
       
        print(f"\nAttempting to borrow '{book1.title}' for Bob...")
        loan2 = Loan("L002", book1, member2, date.today()) 

    except BookUnavailableError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
