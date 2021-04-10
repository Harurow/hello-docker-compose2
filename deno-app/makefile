DOCKER_COMPOSE:=docker-compose
DOCKER_COMPOSE_FILE:=docker-compose.yml
DOCKER_COMPOSE_OVERRIDE_FILE:=docker-compose.override.yml
DOCKER_COMPOSE_DEBUG_FILE:=docker-compose.debug.yml

DAPR_IMAGE:=${DAPR_IMAGE}

.PHONY: build
build:
	$(DOCKER_COMPOSE) build

.PHONY: up
up:
	$(DOCKER_COMPOSE) up -d

.PHONY: debug
debug:
	$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) -f $(DOCKER_COMPOSE_DEBUG_FILE) up --build -d

.PHONY: down
down:
	$(DOCKER_COMPOSE) down

.PHONY: clean
clean:
	$(DOCKER_COMPOSE) down --rmi all --volumes --remove-orphans
