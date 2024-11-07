from django.shortcuts import render
from .models import PageView

def home(request):
    raw_top_pages = PageView.objects.order_by('-views')[:3]
    
    top_pages = []
    for page in raw_top_pages:
        if page.app_name == "search_books" and page.page_name == "search_books":
            display_name = "Search Books"
            display_views = f"閲覧回数: {page.views} 回"
        else:
            display_name = f"{page.app_name} - {page.page_name}"
            display_views = f"Views: {page.views}" if page.views else "閲覧回数なし"

        top_pages.append({
            "display_name": display_name,
            "display_views": display_views,
            "url": page.url if page.url else "#",
            "image_url": page.image_url  # 画像URLを追加
        })

    return render(request, 'home/index.html', {'top_pages': top_pages})
