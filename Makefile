package = flask_template
tests_dir = tests


isort:
	isort -rc $(package)
	isort -rc $(tests_dir)

flake:
	flake8 --exclude $(package)/db/migrations $(package) $(tests_dir)
	if ! isort -c -rc $(package) $(tests_dir); then \
		echo "Import sort errors, run 'make isort' to fix"; \
		isort --diff -rc $(package) $(tests_dir); \
		false; \
	fi

test: flake

clean:
	rm -rf `find . -name __pycache__`
	rm -f `find . -type f -name '*.py[co]' `
	rm -f `find . -type f -name '*~' `
	rm -f `find . -type f -name '.*~' `
	rm -f `find . -type f -name '@*' `
	rm -f `find . -type f -name '#*#' `
	rm -f `find . -type f -name '*.orig' `
	rm -f `find . -type f -name '*.rej' `
	rm -f `find . -type f -name '*.egg-info' `
	rm -f .coverage
	rm -rf coverage
	rm -rf cover
	rm -rf htmlcov
	rm -rf .cache
	rm -rf .eggs
	rm -rf *.egg-info
	rm -rf .pytest_cache

.PHONY: isort flake test clean
