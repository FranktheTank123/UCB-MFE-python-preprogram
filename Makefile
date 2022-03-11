lint:
	black test_game_of_life_RuitongXiao.py
	isort test_game_of_life_RuitongXiao.py
	flake8 test_game_of_life_RuitongXiao.py

test:
	pytest .

lint-check:
	flake8 .
	black . --check
	isort . --check
	