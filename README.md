# CRUD-Django

# Prerequisites
You need to have python 3.9.13 minimun verison installed

## Create and activae your Python Virtual Env
```
#Create virtual env
python -m venv venv

#Activate your virtual env
Unix or Mac os: source venv/bin/activate
Windows PS1: ./venv/Scripts/activate.ps1
Windows Bat: ./venv/Scripts/activate.bat
```

## Install thir party dependencies

- Django: `pip install "Django==4.1"`
- Django Bootstrap v5: `pip install django-bootstrap-v5`
- Django crispy Forms: `pip install django-crispy-forms`
- Cripy Bootstrap 5: `pip install crispy-bootstrap5`

### Or you can choose to install the requirements of this file:
`pip install -r requirements.txt`

## Create Models and Apply changes in generic DB
`python manage.py makemigrations agendapp`
`python manage.py migrate`

## Run Server
`python manage.py runserver`