#!/bin/bash

CONTAINER_NAME=brmed_local_django
IMAGE_NAME=brmed_local_django
DOCKER_FILE=./compose/local/django/Dockerfile
DOCKER_COMPOSE_FILE=local.yml
USER_ID=$(shell id -u)
GROUP_ID=$(shell id -g)
USER_NAME=$(shell id -u -n)
GROUP_NAME=$(shell id -g -n)

## @ Start project
.PHONY: install up_all down_all build_image restart up_db
install: up_all migration create_django_superuser # Generate the backend image and upload ALL containers in the project

up_all: ## Starts ALL containers in the project
	@docker-compose -f ${DOCKER_COMPOSE_FILE} up -d --build

down_all: ## Stop ALL containers in the project
	@docker-compose -f ${DOCKER_COMPOSE_FILE} down

restart: down_all up_all follow_django

## @ Monitor
.PHONY: follow_django log list_status list_ports
follow_django:  check_django_running ## Monitor django container logs
	@docker logs -f ${CONTAINER_NAME}

log:  check_django_running ## List the last 100 logs from the django container
	@docker-compose -f ${DOCKER_COMPOSE_FILE} logs -f --tail 100

list_status: ## List ports containers
	@docker ps -a --format "table {{.Names}}\t{{.State}}\t{{.RunningFor}}\t{{.Size}}"

list_ports: ## List status containers
	@docker ps -a --format "table {{.Names}}\t{{.Ports}}"


## @ Django commands
.PHONY: create_django_superuser load_fixtures make_migration migration
create_django_superuser: check_django_running ## Create a user admin
	@docker exec -i ${CONTAINER_NAME} sh -c "python superuser.dev.py"

make_migration:
	@docker exec -i  ${CONTAINER_NAME} sh -c "python3 manage.py makemigrations"
	@sleep 10

migration:
	@docker exec -i ${CONTAINER_NAME} sh -c "python3 manage.py migrate"
	@sleep 10

## @ Extras
.PHONY: test bash check_django_running
test: ## Run tests
	@docker exec -i ${CONTAINER_NAME} sh -c "pytest"

bash: check_django_running ## Access bash from django container
	@docker exec -it ${CONTAINER_NAME} /bin/bash

check_django_running:
	@RUNNING=$$(docker ps -f name=${CONTAINER_NAME} --format="{{.ID}}"); \
	echo $${RUNNING}; \
	if [ "$${RUNNING}" = "" ]; then \
		echo "${CONTAINER_NAME} machine must be running to run this command"; \
		exit 1; \
	fi

.PHONY: help
help:
	python help.py
