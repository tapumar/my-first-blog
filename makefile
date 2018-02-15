DEFAULT: run

run:
	python3 manage.py runserver

make:
	python3 manage.py makemigrations

migrate:
	python3 manage.py migrate
