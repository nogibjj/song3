install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	./test_sql.py

format:
	black *.py

lint:
	pylint --disable=R,C query.py

all: install lint test
