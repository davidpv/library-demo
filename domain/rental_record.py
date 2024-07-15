from dataclasses import dataclass
from datetime import datetime
from domain.book import Book
from domain.user import User


@dataclass
class RentalRecord:
    book: Book
    user: User
    rented_at: datetime
    due_date: datetime

    def __repr__(self):
        rented_at = self.rented_at.strftime("%d-%m-%Y")
        left_due_days = (self.due_date-self.rented_at)
        return f"RentalRecord('{self.book.title.value}' rented by {self.user.user_name.value}, on {rented_at} with {left_due_days.days} days due date.)"
