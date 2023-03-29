SHELL := /bin/bash

.PHONY: run-dev build up down clean

DOCKERHUB = tcgdigitalus
IMAGE = intelligent-lims
VERSION = latest

init: clean
	python3 -m venv build/py_env

run-dev: clean init
	source ./build/py_env/bin/activate && pip3 install -r ./build/requirements.txt && python3 ./build/src/main.py; deactivate

build: clean init
	docker buildx build -t $(DOCKERHUB)/$(IMAGE):$(VERSION) --file Dockerfile .

up:
	docker compose up --remove-orphans -d

down:
	docker compose down

upload: 
	docker login && docker push $(DOCKERHUB)/$(IMAGE):$(VERSION)

clean:
	rm -rf build/py_env
