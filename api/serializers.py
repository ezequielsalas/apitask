from rest_framework import serializers

from api.models import Book


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        #fields = ('url', 'username', 'email', 'groups')



