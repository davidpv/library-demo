from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class BookId:
    value: UUID


@dataclass(frozen=True)
class BookISBN:
    value: str


@dataclass(frozen=True)
class BookTitle:
    value: str


@dataclass
class Book:
    id: BookId
    isbn: BookISBN
    title: BookTitle
