

setup-dev-repo:
	pip install --user pipenv
	pipenv install --dev

run-tests module="*":
	pipenv run macropython src/pybomination/**/test_{{module}}.py
