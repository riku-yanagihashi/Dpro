import requests
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login/')
def index(request):
    return render(request, 'search_books/search_books.html')

def search_books(request):
    query = request.GET.get('query', '')  # フォームから検索クエリを取得
    books = []

    if query:
        api_key = 'AIzaSyB8cpqf_6umrlXUCRYJ3NmkDJpHQ2g_Xvo'
        url = f'https://www.googleapis.com/books/v1/volumes?q={query}&key={api_key}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            books = data.get('items', [])

    return render(request, 'search_books/search_books.html', {'books': books, 'query': query})
