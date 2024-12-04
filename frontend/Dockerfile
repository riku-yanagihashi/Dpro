# Node.js の公式イメージを使用
FROM node:20-alpine

# 作業ディレクトリを設定
WORKDIR /frontend

# 依存関係ファイルをコピー
COPY package.json package-lock.json ./

# 依存関係をインストール
RUN npm install

# アプリケーションコードをコピー
COPY . .

# React アプリをビルド
RUN npm run build

# ポートを指定
EXPOSE 3000

# アプリケーションを起動
CMD ["npm", "start"]
