from django.urls import path
from . import views

app_name = 'search_books'

urlpatterns = [
    path('', views.index, name='index'),  # トップページとしてindexビューを設定
    path('search/', views.search_books, name='search_books'),
]
