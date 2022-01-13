lint:
	black test_game_of_life.py
	isort test_game_of_life.py
	flake8 test_game_of_life.py


lint-check:
	black . --check
	isort . --check
	flake8 .


test:
	pytest .