from django.urls import path
from .views import BookListCreate, BookDetailView
from .auth_views import RegisterView
from rest_framework.authtoken.views import obtain_auth_token

"""
Defines URL routes for the Book API endpoints.
"""

urlpatterns = [
    path('books/', BookListCreate.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('token/', obtain_auth_token, name='api-token'),
]
