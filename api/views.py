from rest_framework import viewsets
from rest_framework.views import APIView

from api.models import Book
from api.serializers import BookSerializer


class BookView(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
