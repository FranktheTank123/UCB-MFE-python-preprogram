clean: clean-pyc
	conda remove --name lecture_5 --all --yes || echo
	echo Run "conda deactivate" to exit from the conda environment

clean-pyc: ## removes pyc files from your local directory
	find . -name '*.pyc' -exec rm -f {} \;
	find . -name '*.pyo' -exec rm -f {} \;

install:
	conda create -n lecture_5 python=3.10 --yes
	source activate lecture_5
	echo Run "source activate lecture_5" activate the conda environment

test:
	flake8 code/lint/flake8.py
	mypy code/lint/mypy.py