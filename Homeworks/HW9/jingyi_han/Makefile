lint:
	black endpoints.py
	isort endpoints.py
	flake8 endpoints.py
	black model_definition.py
	isort model_definition.py
	flake8 model_definition.py

test:
	pytest tests/tests.py

lint-check:
	black endpoints.py --check
	isort endpoints.py --check
	flake8 endpoints.py
	black model_definition.py --check
	isort model_definition.py --check
	flake8 model_definition.py