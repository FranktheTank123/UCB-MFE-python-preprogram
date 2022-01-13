lint:
	black test.py
	isort test.py
	flake8 test.py

test:
	pytest .

lint-check:
	black . --check
	isort . --check
	flake8 .