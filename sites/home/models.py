from django.db import models

class PageView(models.Model):
    app_name = models.CharField(max_length=50)  # アプリ名
    page_name = models.CharField(max_length=50)  # ページ名
    views = models.IntegerField(default=0)  # アクセス数
    url = models.CharField(max_length=100, blank=True)  # URLを追加

    def __str__(self):
        return f"{self.app_name} - {self.page_name}: {self.views} views"
