# Library Demo

This is a simple Python application that demonstrates the functionality of a library management system. It allows you to add books and users, rent books to users, return rented books, and check for overdue rentals.

## Features

- Add new books with a title and ISBN
- Add new users with a name
- Rent books to users for a specified period (default: 14 days)
- Return rented books
- Get a list of overdue rentals
- Get rentals by user

## Project Structure

- `application/rental_service.py`: Contains the `RentalService` class that handles the business logic for managing books, users, and rentals.
- `domain/book.py`: Defines the `Book` class and related data classes for book ID, ISBN, and title.
- `domain/user.py`: Defines the `User` class and related data classes for user ID and name.
- `domain/rental_record.py`: Defines the `RentalRecord` class that represents a book rental.
- `infrastructure/repositories.py`: Contains repository classes for books, users, and rentals.
- `demo.py`: A demo script that showcases the usage of the library management system.

## Usage

1. Make sure you have Python installed on your system.
2. Clone or download the project repository.
3. Navigate to the project directory.
4. Run the `demo.py` script:

```
Author: David Pérez
```

