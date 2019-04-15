from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from api.models import Book, Author
from api.serializers import BookSerializer


from django.test import TestCase
from api.services import *


# tests for views

class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_book(name="", isbn="", authors=None, number_of_pages=None, publisher="", country="", release_date=None):
        b = Book.objects.create(
            name=name,
            isbn=isbn,
            number_of_pages=number_of_pages,
            publisher=publisher,
            country=country,
            release_date=release_date,
        )
        b.authors.set(authors if authors else [])

    def setUp(self):
        # add test data
        authors = [Author.objects.create(name="George R. R. Martin")]

        self.create_book(name="A Game of Thrones", isbn="978-0553103540", authors=authors, number_of_pages=694,
                         publisher="Bantam Books", country="United States", release_date="1996-08-01")

        self.create_book(name="A Clash of Kings", isbn="978-0553108033", authors=authors, number_of_pages=768,
                         publisher="Bantam Books", country="United States", release_date="1999-02-02")

        self.create_book(name="A Storm of Swords", isbn="978-0553106633", authors=authors, number_of_pages=992,
                         publisher="Bantam Books", country="United States", release_date="2000-10-31")

        self.create_book(name="The Hedge Knight", isbn="978-0976401100", authors=authors, number_of_pages=164,
                         publisher="Dabel Brothers Publishing", country="United States",
                         release_date="2005-03-09")

        self.create_book(name="A Feast for Crows", isbn="978-0553801507", authors=authors, number_of_pages=784,
                         publisher="Bantam Books", country="United Status", release_date="2005-11-08")

        self.create_book(name="The Sworn Sword", isbn="978-0785126508", authors=authors, number_of_pages=152,
                         publisher="Marvel", country="United States", release_date="2008-06-18")


class BooksTest(BaseViewTest):

    def test_get_all_books(self):
        """
        This test ensures that all books added in the setUp method
        exist when we make a GET request to the books/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            # reverse("books-all", kwargs={"version": "v1"})
            reverse("books")
        )
        # fetch the data from db
        expected = Book.objects.all()
        serialized = BookSerializer(expected, many=True)
        self.assertEqual(response.data['data'], serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_book(self):
        """
        This test ensures that all books added in the setUp method
        exist when we make a GET request to the books/ endpoint
        """

        # authors = [Author.objects.create(name="George R. R. Martin")]
        authors = [{"name": "George R. R. Martin"}]

        book = {
            "name": "A Game of Thrones",
            "isbn": "123-9999999990",
            "authors": authors,
            "number_of_pages": 694,
            "publisher": "Bantam Books",
            "country": "United States",
            "release_date": "1996-08-01"
        }

        # hit the API endpoint
        response = self.client.post(reverse("books"), book, format='json')
        # fetch the data from db
        expected = Book.objects.get(isbn="123-9999999990")
        serialized = BookSerializer(expected, many=False)
        self.assertEqual(response.data['data']['book'], serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_book(self):
        """
        This test ensures that a book is updated when we make a PATCH request to the book/:pk endpoint
        """
        expected = Book.objects.get(isbn='978-0553103540')

        expected.name = "A Game of Thrones 2"
        expected.isbn = "123-9999999990"
        expected.number_of_pages = 695

        # hit the API endpoint
        response = self.client.patch(reverse("book", None, [expected.pk]), {
            "name": expected.name,
            "isbn": expected.isbn,
            "number_of_pages": expected.number_of_pages,
        }, format='json')
        # fetch the data from db
        serialized = BookSerializer(expected, many=False)
        self.assertEqual(response.data['data']['book'], serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_book(self):
        """
        This test ensures a deleted book no longer exists
        when we make a DELETE request to the book/:pk endpoint
        """
        expected = Book.objects.get(isbn='978-0553103540')

        # hit the API endpoint
        response = self.client.delete(reverse("book", None, [expected.pk]))

        # fetch the data from db
        # serialized = BookSerializer(expected, many=False)
        with self.assertRaises(Book.DoesNotExist) as ctx:
            Book.objects.get(pk=expected.pk)

        self.assertEqual(response.status_code, status.HTTP_200_OK)


# models test
class ExternalApiTest(TestCase):
    def test_get_all_books_returns_list(self):
        books = get_books({})
        self.assertTrue(type(books) == list)
