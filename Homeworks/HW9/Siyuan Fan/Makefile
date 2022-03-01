lint:
	black ./real_app
	isort ./real_app
	black ./tests
	isort ./tests

pytest:
	pytest tests/tests.py

lint-check:
	black ./real_app --check
	isort ./real_app --check
	black ./tests --check
	isort ./tests --check

run:
	python real_app/model_training.py --data-path "sqlite:////Users/Siyuan Fan/myproject/data/data.db" --model-path "/Users/Siyuan Fan/myproject/data/trained_model.pckl"
	set FLASK_APP=real_app/endpoints.py
	set FLASK_ENV=dvelopment
	set PYTHONPATH=./real_app
	flask run