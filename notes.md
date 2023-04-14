# Packages
python -m venv drf_venv
pip install django
pip install python-dotenv
pip install djangorestframework
pip install black
pip install flake8



# Commands
django-admin startproject drfecommerce
python manage.py runserver
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())


