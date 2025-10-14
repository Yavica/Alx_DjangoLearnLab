from django.urls import path
from .views import BookListCreate, BookDetailView

"""
Defines URL routes for the Book API endpoints.
"""

urlpatterns = [
    path('books/', BookListCreate.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
]
