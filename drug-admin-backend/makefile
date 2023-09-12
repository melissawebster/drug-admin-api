
run:
	poetry run uvicorn app.main:app --host 0.0.0.0

alembic-revision:
	alembic revision --autogenerate -m "first migration"

alembic-head:
	alembic upgrade head