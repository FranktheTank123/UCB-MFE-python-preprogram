lint:
	black test_game_of_life_sl.py
	isort test_game_of_life_sl.py
	flake8 test_game_of_life_sl.py

test:
	pytest .

lint-check:
	black . --check
	isort . --check
	flake8 .