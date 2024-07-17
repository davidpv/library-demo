from application.rental_service import RentalService
from infrastructure.repositories import BookRepository, UserRepository, RentalRepository

book_repo = BookRepository()
user_repo = UserRepository()
rental_repo = RentalRepository()
library_service = RentalService(book_repo, user_repo, rental_repo)

# Add books
book1 = library_service.add_book("Puedes hacerme lo que quieras", "9780743273565")
book2 = library_service.add_book("Mujeres que arden", "9780446310789")
book3 = library_service.add_book("Entra por detrás", "9780446980789")

# Add users
user1 = library_service.add_user("Joan Pastor")
user2 = library_service.add_user("David Perez")

# Rent books
rental1 = library_service.rent_book(book1.id, user1.user_id)
rental2 = library_service.rent_book(book3.id, user1.user_id)
rental3 = library_service.rent_book(book2.id, user2.user_id)

print(f"Rental 1: {rental1}")
print(f"Rental 2: {rental2}")
print(f"Rental 3: {rental3}")

# Return a book
returned = library_service.return_book(book1.id)
print(f"Book 1 returned: {returned}")

# Check overdue rentals
overdue = library_service.get_overdue_rentals()
print(f"Overdue rentals: {overdue}")

# Get rentals by user
user_rentals = library_service.get_rentals_by_user(user1.user_id)
print(f"Rentals by user {user1.user_name.value}: {user_rentals}")

