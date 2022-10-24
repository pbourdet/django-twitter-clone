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

