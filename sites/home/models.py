from django.db import models

class PageView(models.Model):
    app_name = models.CharField(max_length=50)  # アプリ名
    page_name = models.CharField(max_length=50)  # ページ名
    views = models.IntegerField(default=0)  # アクセス数
    url = models.URLField(blank=True, null=True)  # ページのURL
    image_url = models.URLField(blank=True, null=True)  # 画像のURL

    def __str__(self):
        return f"{self.app_name} - {self.page_name}: {self.views} views"


class Inquiry(models.Model):
    name = models.CharField(max_length=255, verbose_name="お名前")
    email = models.EmailField(verbose_name="メールアドレス")
    message = models.TextField(verbose_name="お問い合わせ内容")
    submitted_at = models.DateTimeField(auto_now_add=True, verbose_name="送信日時")

    def __str__(self):
        return f"{self.name} ({self.email})"

