from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# カスタムユーザーモデルの管理画面登録
admin.site.register(CustomUser, UserAdmin)
