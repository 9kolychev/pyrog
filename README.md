# PyRog PROJECT

***pie shop***

## poetry command

```
poetry new pyrog
poetry env use python3.11
poetry shell - (pip): source env/bin/activate
poetry run python (uvicorn, celery)
poetry add fastapi
poetry add black --group dev
poetry show --tree
poetry show --latest
poetry env info
deactivate
```

```
python3.8 -m venv venv
source venv/bin/activate
```

## poetry command

## NGINX
## Uvicorn - ASGI
```
uvicorn main:app --reload
```

- which python
- alembic revision --autogenerate -m "Database creation"
- sudo ss -lptn 'sport = :5432'
- sudo kill pid


## Docker
```
docker-compose -f docker-compose-local.yaml up -d
```

## Alembic migrations
```
alembic init migrations
alembic revision --autogenerate -m "comment"
alembic upgrade heads
```

```python
import sqlite3 as sq

con = sq.connect("saper.db")
cur = con.cursor()

cur.execute("""
""")

con.close()
```
