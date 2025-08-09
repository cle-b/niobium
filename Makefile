.PHONY: setup format lint typing check firefox testfirefox chrome testchrome clean

setup:
	python -m pip install pip --upgrade
	python -m pip install setuptools wheel --upgrade
	pip install -e .
	pip install -r requirements-dev.txt

format:
	black niobium tests

lint:
	black --check niobium tests
	flake8 niobium tests


typing:
	mypy

check: lint typing

firefox:
	docker compose up -d selenium-firefox

testfirefox:	
	pytest -v tests/ --driver Remote --capability browserName firefox --website http://website/ -x 

chrome:
	docker compose up -d selenium-chrome

testchrome:
	pytest -v tests/ --driver Remote --capability browserName chrome --website http://website/ -x 

clean:
	rm -rf .pytest_cache
	rm -rf __pycache__
	rm -rf *.egg-info
	rm -rf venv
	rm -rf build
	rm -rf dist
