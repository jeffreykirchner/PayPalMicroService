python manage.py migrate
python manage.py collectstatic
gunicorn --bind=0.0.0.0 --timeout 30 --max-requests 500 --max-requests-jitter 10  ESIPayPalMS.wsgi
