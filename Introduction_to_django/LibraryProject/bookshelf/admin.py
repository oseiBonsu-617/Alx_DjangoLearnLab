from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Book)
class Book(admin.ModelAdmin):
    list_display = ['title', 'author', 'publication_year']
    list_per_page = 10
    list_filter = ['author', 'publication_year']
    search_fields = ['title', 'author__istartswith', 'publication_year__istartswith']


