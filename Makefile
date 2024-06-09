PYTHON=python3

DC=docker compose


# --================ App ================--
.PHONY: app-run
app-run:
	$(PYTHON) ./src/main.py


# --================ Code Style ================--
.PHONY: style-run
style-run:
	black . && isort . && ruff . && mypy . && pip check


# --================ Docker ================--
.PHONY: docker
docker:
	$(DC) up -d --build

.PHONY: docker-build
docker-build:
	$(DC) build

.PHONY: docker-up
docker-up:
	$(DC) up -d

.PHONY: docker-stop
docker-stop:
	$(DC) stop

.PHONY: docker-start
docker-start:
	$(DC) start

.PHONY: docker-down
docker-down:
	$(DC) down

.PHONY: docker-down-v
docker-down-v:
	$(DC) down -v

.PHONY: docker-logs
docker-logs:
	$(DC) logs

.PHONY: docker-logs-f
docker-logs-f:
	$(DC) logs -f
