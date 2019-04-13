from django.contrib import admin

# Register your models here.
from api.models import Book, Author, BookAuthor

admin.site.register(Book)
admin.site.register(BookAuthor)
admin.site.register(Author)