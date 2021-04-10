.PHONY: build
build:
	pushd dapr-components && make build && popd
	pushd deno-app        && make build && popd
	pushd node-app        && make build && popd
	pushd python-app      && make build && popd
	pushd go-app          && make build && popd

.PHONY: debug
debug:
	pushd dapr-components && make up    && popd
	pushd deno-app        && make debug && popd
	pushd node-app        && make debug && popd
	pushd python-app      && make debug && popd
	pushd go-app          && make debug && popd

.PHONY: up
up:
	pushd dapr-components && make up && popd
	pushd deno-app        && make up && popd
	pushd node-app        && make up && popd
	pushd python-app      && make up && popd
	pushd go-app          && make up && popd

.PHONY: down
down:
	pushd dapr-components && make down && popd
	pushd deno-app        && make down && popd
	pushd node-app        && make down && popd
	pushd python-app      && make down && popd
	pushd go-app          && make down && popd

.PHONY: clean
clean:
	pushd dapr-components && make clean && popd
	pushd deno-app        && make clean && popd
	pushd node-app        && make clean && popd
	pushd python-app      && make clean && popd
	pushd go-app          && make clean && popd
