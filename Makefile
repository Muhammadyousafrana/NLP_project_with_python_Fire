install:
	pip install --upgrade pip && \
	pip install -r requirements.txt &&\
	python -m textblob.download_corpora



test:
	pytest -vvv test_hello.py

lint:
	pylint --disable=R,C hello.py

format:
	code *.py
all: install test lint format