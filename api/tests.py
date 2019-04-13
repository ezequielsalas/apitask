from django.test import TestCase


from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Book
from .serializers import BookSerializer
from datetime import datetime



class BookViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_book(name="", isbn="", number_of_pages=0, publisher="", country="", release_date=datetime.now()):
        Book.objects.create(name=name, isbn=isbn, number_of_pages=number_of_pages, publisher=publisher, country=country,
                            release_date=release_date)

    def setUp(self):
        self.create_book("Harry Potter",isbn="123-3213243569")