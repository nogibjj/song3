install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv test_sql.py

format:
	black *.py

lint:
	pylint --disable=R,C query.py

all: install lint test
