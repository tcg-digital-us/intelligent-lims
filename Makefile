SHELL := /bin/bash

.PHONY: run-dev build up down

run-dev:
	source ./env/bin/activate && pip install -r ./build/requirements.txt && python ./build/src/main.py; deactivate

build:
	docker buildx build -t tcgdigitalus/intelligent-lims:latest --file Dockerfile .

up:
	docker compose up --remove-orphans -d

down:
	docker compose down

