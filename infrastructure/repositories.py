from typing import List, Dict, Optional, Union
from domain.book import Book, BookId
from domain.user import User, UserId
from domain.rental_record import RentalRecord


class BookRepository:
    def __init__(self):
        self.books: List[Book] = []

    def add(self, book: Book):
        self.books.append(book)

    def get_by_id(self, book_id: BookId) -> Optional[Book]:
        return next((b for b in self.books if b.id == book_id), None)

    def get_all(self) -> List[Book]:
        return self.books


class UserRepository:
    def __init__(self):
        self.users: List[User] = []

    def add(self, user: User):
        self.users.append(user)

    def get_by_id(self, user_id: UserId) -> Optional[User]:
        return next((u for u in self.users if u.user_id == user_id), None)

    def get_all(self) -> List[User]:
        return self.users


class RentalRepository:
    def __init__(self):
        self.rentals: Dict[BookId, RentalRecord] = {}

    def add(self, rental: RentalRecord):
        self.rentals[rental.book.id] = rental

    def remove(self, book_id: BookId):
        if book_id in self.rentals:
            del self.rentals[book_id]

    def get_by_book_id(self, book_id: BookId) -> Optional[RentalRecord]:
        return self.rentals.get(book_id)

    def get_all(self) -> List[RentalRecord]:

    def get_by_user_id(self, user_id: UserId) -> List[RentalRecord]:
        return [rental for rental in self.rentals.values() if rental.user.user_id == user_id]
        return list(self.rentals.values())
