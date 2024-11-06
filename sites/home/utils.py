from .models import PageView

def update_page_views(app_name, page_name):
    page_view, created = PageView.objects.get_or_create(
        app_name=app_name,
        page_name=page_name,
        defaults={'views': 0}
    )
    page_view.views += 1
    page_view.save()
