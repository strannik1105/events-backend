PYTHON=python3

DC_LOCAL=docker compose -f docker-compose.local.yaml


# --================ App ================--
.PHONY: app-run
app-run:
	$(PYTHON) ./src/main.py


# --================ Code Style ================--
.PHONY: style-run
style-run:
	black . && isort . && ruff check . && mypy . && pip check


# --================ Docker ================--
.PHONY: docker-local
docker-local:
	$(DC_LOCAL) up -d --build

.PHONY: docker-local-build
docker-local-build:
	$(DC_LOCAL) build

.PHONY: docker-local-up
docker-local-up:
	$(DC_LOCAL) up -d

.PHONY: docker-local-stop
docker-local-stop:
	$(DC_LOCAL) stop

.PHONY: docker-local-start
docker-local-start:
	$(DC_LOCAL) start

.PHONY: docker-local-down
docker-local-down:
	$(DC_LOCAL) down

.PHONY: docker-local-down-v
docker-local-down-v:
	$(DC_LOCAL) down -v

.PHONY: docker-local-logs
docker-local-logs:
	$(DC_LOCAL) logs

.PHONY: docker-local-logs-f
docker-local-logs-f:
	$(DC_LOCAL) logs -f
