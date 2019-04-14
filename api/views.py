from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView
from rest_framework import status

from api import services
from api.models import Book
from api.serializers import BookSerializer


class BookView(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    @staticmethod
    def get_object(pk):

        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return None

    def get(self, request, pk=None):
        response = dict()
        response['status_code'] = status.HTTP_200_OK
        response['status'] = 'success'

        if pk:
            book_instance = self.get_object(pk)
            if book_instance:
                response['data'] = BookSerializer(book_instance).data
                return Response(response)
            else:
                response['status_code'] = status.HTTP_404_NOT_FOUND
                response['status'] = 'failed'
                response['message'] = 'Book not found'
                return Response(response)

        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)

        if not serializer:
            response['data'] = []
            return Response(response)

        response['data'] = serializer.data

        return Response(response)

    def post(self, request):
        book = json.loads(request.body.decode('utf-8'))
        response = dict()

        if book is None:
            return Response(status.HTTP_404_NOT_FOUND)

        serializer = BookSerializer(data=book)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
            response['status_code'] = status.HTTP_201_CREATED
            response['status'] = 'success'
            response['data'] = {'book': BookSerializer(article_saved).data}
        return Response(response)

    def patch(self, request, pk=None):
        response = {}
        book = json.loads(request.body.decode('utf-8'))

        book_instance = self.get_object(pk)
        if book_instance is None:
            response['status_code'] = status.HTTP_404_NOT_FOUND
            response['status'] = 'failed'
            response['message'] = 'Book not found'
            return Response(response)

        serializer = BookSerializer(book_instance, data=book, partial=True)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
            response['status_code'] = status.HTTP_201_CREATED
            response['status'] = 'success'
            response['message'] = 'The book My First Book was updated successfully'
            response['data'] = {'book': BookSerializer(article_saved).data}

        return Response(response)

    def delete(self, request, pk=None):
        response = {}

        book_instance = self.get_object(pk)
        if book_instance:
            book_instance.delete()
            response['status_code'] = status.HTTP_204_NO_CONTENT
            response['status'] = 'success'
            response['message'] = "The book My First Book was deleted successfully"
            response['data'] = []

        return Response(response)


@api_view(['GET'])
def get_book_by_name(request):
    response = dict()
    response['status_code'] = status.HTTP_200_OK
    response['status'] = 'success'

    response['data'] = services.get_books(request.GET)
    return Response(response)
