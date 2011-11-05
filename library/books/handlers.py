from piston.handler import BaseHandler

from books.models import Book, Shelf


class ShelfHandler(BaseHandler):
    model = Shelf


class BookHandler(BaseHandler):
    model = Book
