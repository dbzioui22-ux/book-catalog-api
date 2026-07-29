from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'isbn', 'published_date']

    def validate_isbn(self, value):
        # remove dashes and spaces in case user enters formatted isbn
        cleaned = value.replace('-', '').replace(' ', '')
        if not cleaned.isdigit():
            raise serializers.ValidationError("ISBN must contain only digits.")
        if len(cleaned) not in (10, 13):
            raise serializers.ValidationError("ISBN must be 10 or 13 digits long.")
        return cleaned
