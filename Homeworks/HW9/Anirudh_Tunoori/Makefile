
lint:
	black real_app/endpoints.py real_app/model_training.py
	isort real_app/endpoints.py real_app/model_training.py
	flake8 real_app/endpoints.py real_app/model_training.py

lint-check:
	black . --check
	isort . --check
	flake8 .