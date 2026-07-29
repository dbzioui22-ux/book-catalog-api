from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Book


class BookModelTest(TestCase):

    def setUp(self):
        self.book = Book.objects.create(
            title="Django for Beginners",
            author="William S. Vincent",
            isbn="9781735467221",
            published_date="2022-01-01"
        )

    def test_book_creation(self):
        self.assertEqual(self.book.title, "Django for Beginners")
        self.assertEqual(self.book.author, "William S. Vincent")
        self.assertEqual(self.book.isbn, "9781735467221")

    def test_book_str(self):
        self.assertEqual(str(self.book), "Django for Beginners by William S. Vincent")


class BookAPITest(APITestCase):

    def setUp(self):
        self.book = Book.objects.create(
            title="Test Driven Development",
            author="Kent Beck",
            isbn="9780321146533",
            published_date="2002-11-18"
        )

    def test_create_book(self):
        data = {
            "title": "Clean Code",
            "author": "Robert C. Martin",
            "isbn": "9780132350884",
            "published_date": "2008-08-01"
        }
        response = self.client.post('/api/books/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_list_books(self):
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_book(self):
        response = self.client.delete(f'/api/books/{self.book.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_invalid_isbn(self):
        data = {
            "title": "Bad Book",
            "author": "Nobody",
            "isbn": "123",  # too short, should be rejected
            "published_date": "2023-01-01"
        }
        response = self.client.post('/api/books/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
