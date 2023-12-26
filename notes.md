# Packages
python -m venv drf_venv
pip install django
pip install python-dotenv
pip install djangorestframework
pip install pytest
pip install pytest-django #optional
pip install black
pip install flake8
pip install django-mptt  # for many to many relationship b/w the tables
pip install drf-spectacular # for collecting all information of the API
pip install coverage
pip install pytest-coverage # similar to coverage package 
pip install pytest-factoryboy



# Commands
django-admin startproject drfecommerce
python manage.py runserver
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
python manage.py startapp product ./drfecommerce/product
pytest
pytest -h
coverage 
coverage run -m pytest               # to check where test required
coverage html                        # for generating html test reports
pytest --cov     # same output as with coverage run -m pytest





