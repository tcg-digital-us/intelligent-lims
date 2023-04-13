SHELL := /bin/bash

.PHONY: run-dev build up down upload clean

DOCKERHUB = tcgdigitalus
IMAGE = intelligent-lims
VERSION = latest

PYTHON_COMMAND = $(shell python ./scripts/get_py.py)

ifeq ($(PYTHON_COMMAND),null)
	$(error Python 3 not found. Please install Python 3 and try again.)
endif

clean:
	@$(PYTHON_COMMAND) ./scripts/clean.py
	@echo Cleaned project.

init:
	@echo Initializing virtual environment...
	@$(PYTHON_COMMAND) ./scripts/init_venv.py
	@echo Initialization complete.

run_dev: clean
	@echo Running project locally...
	@$(PYTHON_COMMAND) ./scripts/run_dev.py

dockerimage: clean
	@docker buildx build -t $(DOCKERHUB)/$(IMAGE):$(VERSION) --file Dockerfile .

upload: dockerimage 
	@docker login && docker push $(DOCKERHUB)/$(IMAGE):$(VERSION)

up:
	@docker compose up --remove-orphans -d

down:
	@docker compose down

apply:
	@sudo kubectl apply -f k8s-deploy.yml

delete:
	@kubectl delete -f k8s-deploy.yml
