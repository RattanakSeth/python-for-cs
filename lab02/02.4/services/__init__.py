from .book import BookService

write_to_json = BookService().write_to_json
read_from_json = BookService().read_from_json

__all__ = ['write_to_json', 'read_from_json']