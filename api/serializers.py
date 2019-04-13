from rest_framework import serializers

from api.models import Book


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ('id','name', 'isbn', 'number_of_pages', 'publisher', 'country', 'release_date')



