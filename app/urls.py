from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('posts/', posts, name='posts'),
    path('search_posts/', search_posts, name='search_posts'),
    path('post/<int:id>/', post_detail, name="post_detail"),
    path('trend/<int:id>/', trend_detail, name="trend_detail"),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]
