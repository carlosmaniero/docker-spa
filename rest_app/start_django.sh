python3 manage.py migrate
gunicorn rest_app.wsgi:application --bind 0.0.0.0:8080 --workers 3
