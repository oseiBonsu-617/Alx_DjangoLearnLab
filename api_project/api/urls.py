from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register('books_all', views.BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', views.BookList.as_view(), name='book-list'),
    # path('books_a/', views.BookListCreatAPIView.as_view(), name='post-list-create'),
    # path('books/<int:pk>', views.BookRetrieveUpdateDestroyAPIView.as_view(), name='post-retrieve-update-destroy'),
    path(r'', include(router.urls)),
]
