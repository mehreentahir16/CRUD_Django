# CRUD_Django
This is a simple example explaining CRUD operations in Django

Example contains the implemention of CRUD operations using Function Based Views and Class Based Views in Djnago. 

CRUD_FBVs(implementing Function Based Views) uses the built-in user Model by Django. You can also append 

LOGIN_URL = '/admin/login/'

to settings.py, create super user by 'python manage.py createsuperuser' and use superuser to access this functionality or 
feel free to extend the repo.

IF you want to test the CRUD_CBVs(implementing Class Based Views) you can add user as Foreing key to movie model and use it same as CRUD_FBVs
