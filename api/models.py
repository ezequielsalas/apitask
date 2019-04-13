from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return "{}".format(self.name)


class Book(models.Model):
    name = models.CharField(max_length=250)
    isbn = models.CharField(max_length=50)
    authors = models.ManyToManyField(Author, through='BookAuthor', through_fields=('book', 'author'), )
    number_of_pages = models.IntegerField()
    publisher = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    release_date = models.DateField()

    def __str__(self):
        return "{}".format(self.name)


class BookAuthor(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
