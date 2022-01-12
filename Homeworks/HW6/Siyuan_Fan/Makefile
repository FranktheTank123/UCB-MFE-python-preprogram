lint-check:
        python3.7 -m black test_game_of_life.py --check
        isort test_game_of_life.py --check
        flake8 --max-line-length=100 --ignore=E128 test_game_of_life.py
        mypy test_game_of_life.py --check

lint:
        python3.7 -m black test_game_of_life.py
        isort test_game_of_life.py
        flake8 --max-line-length=100 --ignore=E128 test_game_of_life.py
        mypy test_game_of_life.py

test:
        pytest test_game_of_life.py
