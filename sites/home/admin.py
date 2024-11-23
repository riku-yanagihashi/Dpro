from django.contrib import admin
from .models import PageView
from .models import Inquiry

@admin.register(PageView)
class PageViewAdmin(admin.ModelAdmin):
    list_display = ('app_name', 'page_name', 'views', 'url', 'image_url')
    search_fields = ('app_name', 'page_name')
    list_filter = ('app_name',)
    ordering = ('-views',)

class InquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'submitted_at')  # 一覧画面で表示するフィールド
    search_fields = ('name', 'email')  # 検索可能なフィールド
    list_filter = ('submitted_at',)  # フィルタリング可能なフィールド
    ordering = ('-submitted_at',)  # デフォルトの並び順（新しい順）


admin.site.register(Inquiry, InquiryAdmin)
