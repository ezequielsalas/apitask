from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from api.models import Book, Author, BookAuthor


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ('name',)


class BookSerializer(serializers.HyperlinkedModelSerializer):

    authors = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = ('id','name', 'isbn',  'authors', 'number_of_pages', 'publisher', 'country', 'release_date')


    def create(self, validated_data):
        author_data = validated_data.pop('authors')
        book = Book.objects.create(**validated_data)

        for aut in author_data:
            author, _ = Author.objects.get_or_create(**aut)
            BookAuthor.objects.create(book=book, author=author)
        return book
