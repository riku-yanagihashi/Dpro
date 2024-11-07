from django.contrib import admin
from .models import PageView

@admin.register(PageView)
class PageViewAdmin(admin.ModelAdmin):
    list_display = ('app_name', 'page_name', 'views', 'url', 'image_url')
    search_fields = ('app_name', 'page_name')
    list_filter = ('app_name',)
    ordering = ('-views',)
