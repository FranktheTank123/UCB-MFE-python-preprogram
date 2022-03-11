lint:
	black test.py
	isort test.py
	flake8 test.py

test:
	pytest .
	black . --check
	sort . --check
	flake8 .