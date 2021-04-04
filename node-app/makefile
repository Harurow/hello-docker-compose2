DOCKER_COMPOSE:=docker-compose
DOCKER_COMPOSE_FILE:=docker-compose.yml
DOCKER_COMPOSE_OVERRIDE_FILE:=docker-compose.override.yml

DAPR_IMAGE:=${DAPR_IMAGE}

.PHONY: build
build:
	$(DOCKER_COMPOSE) build

.PHONY: up
up:
ifneq ($(DAPR_IMAGE),)
	cp $(DOCKER_COMPOSE_FILE) $(DOCKER_COMPOSE_OVERRIDE_FILE)
	sed -i 's,daprio\/daprd:edge,$(DAPR_IMAGE),g' $(DOCKER_COMPOSE_OVERRIDE_FILE)
endif
	$(DOCKER_COMPOSE) up

.PHONY: run
run:
ifneq ($(DAPR_IMAGE),)
	cp $(DOCKER_COMPOSE_FILE) $(DOCKER_COMPOSE_OVERRIDE_FILE)
	sed -i 's,daprio\/daprd:edge,$(DAPR_IMAGE),g' $(DOCKER_COMPOSE_OVERRIDE_FILE)
endif
	$(DOCKER_COMPOSE) up -d

.PHONY: down
down:
	$(DOCKER_COMPOSE) down --rmi all --volumes --remove-orphans

