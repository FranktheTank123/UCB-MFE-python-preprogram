lint:
	black test_game_of_life_RuitongXiao.py
	isort test_game_of_life_RuitongXiao.py
	flake8 test_game_of_life_RuitongXiao.py

test:
	pytest .

lint-check:
	black . --check
	isort . --check
	flake8 .