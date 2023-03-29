SHELL := /bin/bash

.PHONY: run-dev build up down clean

run-dev: clean
	python3 -m venv build/py_env && source ./build/py_env/bin/activate && pip3 install -r ./build/requirements.txt && python3 ./build/src/main.py; deactivate

build:
	docker buildx build -t tcgdigitalus/intelligent-lims:latest --file Dockerfile .

up:
	docker compose up --remove-orphans -d

down:
	docker compose down

clean:
	rm -rf build/py_env
