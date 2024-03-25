install:
	poetry install

start_debug:
	poetry run python manage.py runserver

start:
	gunicorn welbex.wsgi:application

test:
	poetry run coverage run --source='.' manage.py test

lint:
	poetry run flake8 welbex

build:
	./build.sh
