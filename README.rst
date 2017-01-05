======================
django-heroku-template
======================

A project template for deploying Django 1.8 and Python 3.4 to Heroku (Cedar Stack).

To use this project follow these steps:

#. Create your working environment
#. Install Django
#. Create the new project using the django-heroku-template
#. Install additional dependencies
#. Initialize the local git repository
#. Configure the Heroku application
#. Deploy to Heroku

Working Environment
===================

Virtualenv (with virtualenvwrapper)
-----------------------------------

Use virtualenvwrapper (http://virtualenvwrapper.readthedocs.org/en/latest/)
to create the virtual environments::

    $ mkvirtualenv --python=/usr/bin/python3 myvenv

Install Django
==============

To install Django in the new virtual environment, run the following command::

    $ pip install django==1.8

Create the Project
==================

To create a new Django project called '**myproject**' using
django-heroku-template, run the following command::

    $ django-admin startproject --template=https://github.com/huntedcodes/django-heroku-template/zipball/master --extension=py,rst,html --name=Procfile myproject

Install Dependencies
====================

For local development::

    $ pip install -r requirements/local.txt

For production (automatic on Heroku)::

    $ pip install -r requirements.txt

Initialize the Local Git Repository
===================================

Initialize the local git repository::

    $ git init .
    $ git add .
    $ git commit -m "Initial commit."

Configure The Heroku Application
================================

If you haven't already:

#. Sign up for Heroku (https://signup.heroku.com/)
#. Install the Heroku Toolbelt (https://toolbelt.heroku.com/)

Create the Heroku application::

    $ heroku create myproject

Set the **DJANGO_SETTINGS_MODULE** environment variable::

    $ heroku config:set DJANGO_SETTINGS_MODULE=myproject.settings.production

Set a new **SECRET_KEY_PRODUCTION** environment variable::

    $ heroku config:set SECRET_KEY_PRODUCTION=$(python -c "import random; import string; print (''.join( [random.SystemRandom().choice(string.digits + string.ascii_letters + string.punctuation).replace('\"', '').replace('\'','') for i in range(100)] ))")

Verify the configuration::

    $ heroku config
    
The **DATABASE_URL** environment variable is created after the initial push.

Deploy to Heroku
================

Push the code to the Heroku application::

    $ git push heroku master

Migrate the database::

    $ heroku run python manage.py migrate
    
Create a superuser for the site::

    $ heroku run python manage.py createsuperuser

Check out the deployed site's admin page::

    $ heroku open admin

