# Install dependencies
install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

# Run tests using pytest and generate coverage
test:
	python -m pytest -vv --cov=main --cov=mylib test_*.py

# Run unittests directly
unittest:
	python -m unittest discover -s . -p "test_*.py"

# Format code with black
format:
	black *.py mylib/*.py

# Lint code with ruff (for faster linting)
lint:
	# Disable comment to test speed
	# pylint --disable=R,C --ignore-patterns=test_.*?py *.py mylib/*.py
	# ruff linting is 10-100X faster than pylint
	ruff check *.py mylib/*.py

# Lint Dockerfile with hadolint
container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

# Refactor: run format and lint
refactor: format lint

# Docker build and push
docker-build:
	docker build -t tursunait/spark-python-app:latest .

docker-push: docker-build
	docker push tursunait/spark-python-app:latest

# Deploy target
deploy: docker-build docker-push
	docker run --rm -p 8080:8080 tursunait/spark-python-app:latest

# Run all steps (install, lint, test, format, deploy)
all: install lint test format deploy

# ETL workflow
extract:
	python main.py extract

transform_load: 
	python main.py transform_load

query:
	python main.py general_query "SELECT us.state, round(avg(u.urbanindex)) AS urbanindex FROM default.urbanization_statedb_tt284 us RIGHT JOIN default.urbanizationdb_tt284 u on us.state=u.state group by us.state order by urbanindex desc"
