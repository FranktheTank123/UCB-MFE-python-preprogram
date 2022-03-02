lint:
	black real_app/endpoints.py
	black real_app/model_definition.py
	black real_app/model_training.py
	black tests/test_endpoints.py
	flake8 real_app/endpoints.py
	flake8 real_app/model_definition.py
	flake8 real_app/model_training.py
	flake8 tests/test_endpoints.py
	isort real_app/endpoints.py
	isort real_app/model_definition.py
	isort real_app/model_training.py
	isort tests/test_endpoints.py

test:
	pytest .
