Monitor the health of the Canadian economy in real time with data fetch and data visualization automation

This project was developed in CANDEV data challenge organized by Statistics Canada & University of Ottawa

Dataset: - Consumer Price Index from Statistics Canada

Programming languages & Tools: - Python, Django, Google Charts

Strategies & Techniques: - Automation with Python, Data preprocessing, data visualization using Google charts, Data prediction using machine learning algorithm linear regression

Results: - A web application was developed for data visualization and for predicting the Canadian economy in real time with end-to-end automation.



# MIT Data Annotations

API for the MIT Data Annotations Site

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg)](https://github.com/pydanny/cookiecutter-django/)

## Setup

If you are using Ubuntu/Debian, follow these instructions to get a working environment very quickly.

1. Install [PostgreSQL](http://www.postgresql.org/) and configure it in your system:

    ``` shell
    $ sudo apt-get install postgresql
    $ sudo -u postgres psql
    ```
    ``` sql
    $ create database candev_finstat;
    $ create user candev_finstat with password 'finstatpass' createdb;
    $ grant all privileges on database candev_finstat to candev_finstat;
    $ \q
    ```

2. Install required OS dependencies. For Ubuntu/Debian you can do:

    ``` shell
    $ ./utility/install_os_dependencies.sh install
    ```

3. Set up the environment variables file (.env) in the root directory. You will need to setup at least:
   - DJANGO_READ_DOT_ENV_FILE
   - DATABASE_URL
   - CELERY_BROKER_URL

4. Install required python dependencies. For Ubuntu/Debian you can do:

    ``` shell
    $ sudo pip install pipenv
    $ pipenv install --dev
    $ pipenv shell
    ```

5. Run the DB migrations:

    ``` shell
    $ ./manage.py migrate
    ```

You are done. :)

## Running

``` shell
$ ./manage.py runserver
```

## Testing

``` shell
$ py.test
$ flake8 .
```
