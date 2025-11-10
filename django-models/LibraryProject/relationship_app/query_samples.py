# Query all books by specific author
"""
query_samples.py
----------------
Sample Django ORM queries for the relationship_app.

Queries:
1. Query all books by a specific author.
2. List all books in a library.
3. Retrieve the librarian for a library.
"""

import django
import os
from .models import Author, Book, Library, Librarian

# ✅ Set up Django environment (adjust project name to match your actual Django project)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project_name.settings")
django.setup()


def query_books_by_author(author_name: str):
    """Query all books by a specific author."""
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        print(f"\nBooks by {author.name}:")
        if books.exists():
            for book in books:
                print(f"- {book.title}")
        else:
            print("No books found for this author.")
    except Author.DoesNotExist:
        print(f"No author found with name '{author_name}'.")


def list_books_in_library(library_name: str):
    """List all books in a specific library."""
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        print(f"\nBooks in '{library.name}' Library:")
        if books.exists():
            for book in books:
                print(f"- {book.title}")
        else:
            print("No books available in this library.")
    except Library.DoesNotExist:
        print(f"No library found with name '{library_name}'.")


def retrieve_librarian_for_library(library_name: str):
    """Retrieve the librarian assigned to a specific library."""
    try:
        library = Library.objects.get(name=library_name)
        try:
            librarian = Librarian.objects.get(library=library)
            print(f"\nLibrarian for '{library.name}' Library: {librarian.name}")
        except Librarian.DoesNotExist:
            print(f"'{library.name}' Library has no assigned librarian.")
    except Library.DoesNotExist:
        print(f"No library found with name '{library_name}'.")


if __name__ == "__main__":
    # Example usage (replace these names with ones from your database)
    query_books_by_author("George Orwell")
    list_books_in_library("Central Library")
    retrieve_librarian_for_library("Central Library")
