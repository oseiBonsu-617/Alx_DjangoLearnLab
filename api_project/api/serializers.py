from rest_framework.serializers import ModelSerializer
from .models import Book

class BookSerializer(ModelSerializer):
    model = Book
    fields = '__all__'