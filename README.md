## PYTHON TRAINING #01 About The Project 

Created this project as a training for Python Django

-   Python 3.12
-   Django 5
-   Bootstrap
-   Mysql

## Step-by-step guide to run the project

- Make sure you have a running mysql community server, everything else is already setup in the requirement.txt to make sure that mysql is running on django 5
-   Make sure that python virtual environment is running
- run `pip install -r /path/to/requirements.txt`
- change settings.py sqllite into this
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'CRUDDB', <---- I named my DB like this
        'USER': 'root',
        'PASSWORD': 'rootpass', <---- user password
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```
- run `python mydb.py` to generate db using python shell
- run `python manage.py migrate` to generate table
- run `winpty python manage.py createsuperuser` (windows), remove winpty if in mac or linux (this will create super user )
- finally run `python manage.py runserver`
