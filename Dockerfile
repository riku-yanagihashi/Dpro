# ベースイメージを指定
FROM python:3.12-slim

# 必要なツールをインストール
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    build-essential \
    libffi-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# 作業ディレクトリを設定
WORKDIR /app

# 必要なファイルをコピー
COPY requirements.txt /requirements.txt

# 依存パッケージをインストール
RUN pip install --upgrade pip && pip install -r /requirements.txt

# アプリケーションコードをコピー
COPY ./sites /app

# 環境変数の設定
ENV DJANGO_SETTINGS_MODULE=Dpro.settings
ENV PYTHONUNBUFFERED=1

# エントリーポイントを設定
CMD ["bash", "-c", "python manage.py migrate && python manage.py collectstatic --noinput && python manage.py runserver 0.0.0.0:8000"]
