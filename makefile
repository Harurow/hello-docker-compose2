.PHONY: build
build:
	pushd dapr-components && make build && popd
	pushd deno-app        && make build && popd
	pushd node-app        && make build && popd
	pushd python-app      && make build && popd

.PHONY: run
run:
	pushd dapr-components && make run && popd
	pushd deno-app        && make run && popd
	pushd node-app        && make run && popd
	pushd python-app      && make run && popd

.PHONY: down
down:
	pushd dapr-components && make down && popd
	pushd deno-app        && make down && popd
	pushd node-app        && make down && popd
	pushd python-app      && make down && popd
