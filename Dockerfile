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

# 必要なファイルをコピー (依存パッケージのキャッシュを利用するために分離)
COPY requirements.txt /requirements.txt

# 依存パッケージをインストール
RUN pip install --upgrade pip && pip install -r /requirements.txt

# アプリケーションコードをコピー
COPY ./sites /app

# 環境変数の設定
ENV DJANGO_SETTINGS_MODULE=Dpro.settings
ENV PYTHONUNBUFFERED=1

# エントリーポイントスクリプトをコピー
COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

# デフォルトコマンドを設定
ENTRYPOINT ["/docker-entrypoint.sh"]
