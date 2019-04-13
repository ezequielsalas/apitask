from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=250)


class Book(models.Model):
    name = models.CharField(max_length=250)
    isbn = models.CharField(max_length=50)
    authors = models.ManyToManyField(Author, through='BookAuthor', through_fields=('author', 'book'),)
    number_of_pages = models.IntegerField()
    publisher = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    release_date = models.DateField()


class BookAuthor(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

