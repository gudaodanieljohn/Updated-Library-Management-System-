from exceptions import BookNotFoundError, MemberNotFoundError, BookUnavailableError, LoanNotFoundError
from book import Book
from member import Member
from loan import Loan

class LibraryService:
    def __init__(self):
        self._books = {}
        self._members = {}
        self._loans = []

    def add_book(self, book):
        self._books[book.isbn] = book
        print(f"Book '{book.title}' added successfully.")

    def register_member(self, member):
        self._members[member.member_id] = member
        print(f"Member '{member.name}' registered successfully.")

    def borrow_book(self, member_id, isbn):
        member = self._members.get(member_id)
        if member is None:
            raise MemberNotFoundError(f"Member with ID '{member_id}' not found.")

        book = self._books.get(isbn)
        if book is None:
            raise BookNotFoundError(f"Book with ISBN '{isbn}' not found.")

        if not book.available:
            raise BookUnavailableError(f"Book '{book.title}' is currently unavailable.")

        book.available = False
        member.borrowed_count += 1
        loan = Loan(member_id, isbn)
        self._loans.append(loan)
        return f"You borrowed '{book.title}'."

    def return_book(self, member_id, isbn):
        member = self._members.get(member_id)
        if member is None:
            raise MemberNotFoundError(f"Member with ID '{member_id}' not found.")

        book = self._books.get(isbn)
        if book is None:
            raise BookNotFoundError(f"Book with ISBN '{isbn}' not found.")

        for loan in self._loans:
            if loan.member_id == member_id and loan.isbn == isbn and not loan.returned:
                loan.returned = True
                book.available = True
                member.borrowed_count -= 1
                return f"You returned '{book.title}'."

        raise LoanNotFoundError(f"No active loan found for Member '{member_id}' and Book ISBN '{isbn}'.")

    def view_books(self):
        if not self._books:
            print("No books in the library.")
            return
        print("\n--- Books in Library ---")
        for book in self._books.values():
            book.show_info()

    def view_members(self):
        if not self._members:
            print("No members registered.")
            return
        print("\n--- Library Members ---")
        for member in self._members.values():
            member.show_info()

    def view_loans(self):
        if not self._loans:
            print("No loans recorded.")
            return
        print("\n--- Active Loans ---")
        for loan in self._loans:
            loan.show_info()