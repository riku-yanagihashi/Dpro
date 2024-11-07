from django.urls import reverse
from .models import PageView

# 各ページに対応する画像URLを事前に定義
PAGE_IMAGE_URLS = {
    ('search_books', 'search_books'): 'static/images/feature/book_search.png',
    ('findbook', 'findbook'): 'https://example.com/path/to/findbook_image.jpg',
    ('chatbook', 'chatbook'): 'https://example.com/path/to/chatbook_image.jpg',
    ('gamebook', 'gamebook'): 'https://example.com/path/to/gamebook_image.jpg',
}

def update_page_views(app_name, page_name):
    # 新規作成または既存のページを取得
    page_view, created = PageView.objects.get_or_create(
        app_name=app_name,
        page_name=page_name,
        defaults={
            'views': 0,
            'url': reverse(f"{app_name}:{page_name}"),
            'image_url': PAGE_IMAGE_URLS.get((app_name, page_name), '')  # 画像URLを設定
        }
    )
    
    # ページビュー数を増やし、画像URLがなければ設定
    page_view.views += 1
    if not page_view.image_url:
        page_view.image_url = PAGE_IMAGE_URLS.get((app_name, page_name), '')
    page_view.save()
