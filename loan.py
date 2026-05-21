from datetime import date

class Loan:
    def __init__(self, loan_id, book, member, borrow_date):
        self._loan_id = loan_id
        self._book = book
        self._member = member
        self._borrow_date = borrow_date
        self._return_date = None

        self._book.mark_as_borrowed()

    @property
    def is_active(self):
        return self._return_date is None

    def complete_return(self):
        self._return_date = date.today()
        self._book.mark_as_returned()
        