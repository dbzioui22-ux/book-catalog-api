from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

# TODO: maybe add filtering by author later
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
