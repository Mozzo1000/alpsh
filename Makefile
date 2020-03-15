build:
	python3 -m nuitka --output-dir=dist/ --follow-imports --standalone alpsh/shell.py --lto

test:
	python3 -m unittest

lint:
	flake8 --statistics --output-file=lint_errors.txt --max-line-length=120 --tee 
