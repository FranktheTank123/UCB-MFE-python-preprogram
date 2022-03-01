lint:
	black compare_pipelines.py
	black endpoints.py
	black model_definition.py
	black model_training.py

	isort compare_pipelines.py
	isort endpoints.py
	isort model_definition.py
	isort model_training.py

	flake8 compare_pipelines.py
	flake8 endpoints.py
	flake8 model_definition.py
	flake8 model_training.py

test:
	pytest .

lint-check:
	black . --check
	isort . --check
	flake8 .