lint:
	black test_compare_pipelines.py
	
	isort test_compare_pipelines.py
	
	flake8 test_compare_pipelines.py
	
test:
	pytest .

lint-check:
	black . --check
	isort . --check
	flake8 .