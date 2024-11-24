
```bash
dcud

dcd

# dbをバックアップ
docker exec -it postgres_db pg_dump -U riku dprodb > db_dump.sql

# dbをロード
docker exec -i postgres_db psql -U riku dprodb < db_dump.sql
```
```
```
