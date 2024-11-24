# ベースイメージを指定
FROM python:3.12-slim

# 作業ディレクトリを設定
WORKDIR /app

# 必要なファイルをコピー (依存パッケージのキャッシュを利用するために分離)
COPY requirements.txt /requirements.txt

# 依存パッケージをインストール
RUN pip install --upgrade pip && pip install -r /requirements.txt

# アプリケーションコードをコピー
COPY ./sites /app

# 環境変数の設定
ENV DJANGO_SETTINGS_MODULE=Dpro.settings
ENV PYTHONUNBUFFERED=1

# サーバー起動コマンド
CMD ["bash", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
