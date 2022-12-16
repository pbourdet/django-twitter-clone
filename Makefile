DJANGO_SETTINGS_MODULE ?= project.settings.development

install:
	python3 -m venv .venv
	./.venv/bin/pip install -U pip poetry
	./.venv/bin/poetry install

start:
	docker compose up -d
	sleep 2 #hack to wait db to start before starting server
	DJANGO_SETTINGS_MODULE=${DJANGO_SETTINGS_MODULE} ./.venv/bin/python src/manage.py migrate
	DJANGO_SETTINGS_MODULE=${DJANGO_SETTINGS_MODULE} ./.venv/bin/python src/manage.py runserver

pylint:
	./.venv/bin/python ./.venv/bin/pylint src tests

functional-tests:
	DJANGO_SETTINGS_MODULE=project.settings.test ./.venv/bin/python src/manage.py test --tag functional

unit-tests:
	DJANGO_SETTINGS_MODULE=project.settings.test ./.venv/bin/python src/manage.py test --tag unit

all-tests:
	make unit-tests
	make functional-tests

checks:
	make pylint || true
	make unit-tests
	make functional-tests
