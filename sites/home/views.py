from django.shortcuts import render
from .models import PageView

def home(request):
    # デバッグ用のprint文
    print("homeビューが呼び出されました")
    
    # 上位3件を取得
    top_pages = PageView.objects.order_by('-views')[:3]
    print("取得したトップページ:", top_pages)  # デバッグ用にトップページの内容を出力
    return render(request, 'home/index.html', {'top_pages': top_pages})
