#!/bin/bash
set -e

# データベースが起動するのを待つ
echo "Waiting for the database..."
until nc -z db 5432; do
    sleep 1
done

# データベースマイグレーション
echo "Running migrations..."
python manage.py migrate

# 開発サーバーを起動
echo "Starting Django server..."
exec "$@"

