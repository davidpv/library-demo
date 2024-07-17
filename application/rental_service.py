from datetime import datetime, timedelta
from typing import List, Optional
from uuid import uuid4
from domain.book import Book, BookId, BookTitle, BookISBN
from domain.rental_record import RentalRecord
from domain.user import User, UserId, UserName
from infrastructure.repositories import BookRepository, UserRepository, RentalRepository


class RentalService:

    def __init__(self, book_repo: BookRepository, user_repo: UserRepository, rental_repo: RentalRepository):
        self.book_repo = book_repo
        self.user_repo = user_repo
        self.rental_repo = rental_repo

    def add_book(self, title: str, isbn: str) -> Book:
        book = Book(BookId(uuid4()), BookISBN(isbn), BookTitle(title))
        self.book_repo.add(book)
        return book

    def add_user(self, username: str) -> User:
        user = User(UserId(uuid4()), UserName(username))
        self.user_repo.add(user)
        return user

    def rent_book(self, book_id: BookId, user_id: UserId, rental_period: int = 14) -> Optional[RentalRecord]:
        book = self.book_repo.get_by_id(book_id)
        user = self.user_repo.get_by_id(user_id)

        if not book or not user:
            return None

        if self.rental_repo.get_by_book_id(book_id):
            return None

        rental_record = RentalRecord(
            book=book,
            user=user,
            rented_at=datetime.now(),
            due_date=datetime.now() + timedelta(days=rental_period)
        )
        self.rental_repo.add(rental_record)
        return rental_record

    def return_book(self, book_id: BookId) -> bool:
        if self.rental_repo.get_by_book_id(book_id):
            self.rental_repo.remove(book_id)
            return True
        return False

    def get_overdue_rentals(self) -> List[RentalRecord]:
        now = datetime.now()
        return [rental for rental in self.rental_repo.get_all() if rental.due_date < now]

    def get_rentals_by_user(self, user_id: UserId) -> List[RentalRecord]:
        user = self.user_repo.get_by_id(user_id)
        if not user:
            return []
        return [rental for rental in self.rental_repo.get_all() if rental.user.user_id == user_id]
