lint:
	black test_game_of_life.py
	isort test_game_of_life.py
	flake8 test_game_of_life.py

test:
	pytest test_game_of_life.py

lint-check:
	black . --check
	isort test_game_of_life.py --check
	flake8 .