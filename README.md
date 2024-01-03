# PyRog PROJECT

***pie shop***

```
python3.8 -m venv venv
source venv/bin/activate
which python
uvicorn main:app --reload
sudo ss -lptn 'sport = :5432'
sudo kill pid
```

## Poetry
```
poetry new pyrog
poetry env use python3.11
poetry shell - (pip): source env/bin/activate
poetry run python (uvicorn, celery)
poetry add fastapi
poetry add black --group dev
poetry remove envparse
poetry show --tree
poetry show --latest
poetry env info
deactivate
```

## Alembic
```
alembic init -t async alembic
alembic init migrations
alembic revision --autogenerate -m "comment"
alembic upgrade heads
alembic downgrade base
alembic history
alembic current
```

## Docker
```
docker-compose -f docker-compose-local.yaml up -d
```

## PyTest
```
-s - prints
-v
--durations=3
-vv
pytest -s -v [testpath]
pytest -s -v -k development [testpath]
pytest -s -v -k "not development" [testpath] 
pytest -s -v [testpath] --alluredir=allureress
allure serve allureress
```

## Doker
```
docker build -t automation-tests .
docker build --build-arg run_env=development -t automation-tests .
doker run automation-tests
docer cp $(docker ps -a -q | head -1):/allure-results
```