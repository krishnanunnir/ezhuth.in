# KNODE
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/krishnanunnir/server_monitor_bot/blob/master/LICENSE)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

## django KNODE cms

KNODE is an easy to install cms tool where users can easily setup a new site in less than 5 minutes.

## Commiting

We will be using the angular style of commits <sup>[3](https://github.com/angular/angular/blob/master/CONTRIBUTING.md)</sup>, modified accordingly for our project. Please refer past commits to get an idea

## Running a build on your machine

This will walk you through the process of running this website locally on your machine.

#### Setting up local installation of the Project
Create local copy of the source code using the git clone command. In order to handle the dependencies we setup a virtual environment.
 ```
 git clone https://github.com/krishnanunnir/django-knode-cms.git
 python3 -m venv .envs/knode
 ```
After creating the virtual environment we need to activate it.

```
source ./<venv-folder-name>/bin/activate
```
After activating the virtual environment we need to install the dependencies for the project, which can be done as follows.
```
pip install -r requirements.txt
```
#### Configuring the environment variables

This project uses PostgreSQL as its database management system. We will be using the psycopg database adapter for connecting the Django models to the database. Create your own user and database in postgres for running the project <sup>[2](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04)</sup>. Set a local instance of postgres and configure a user, db and password. Run the initenv.py file to intialize the all environment variables which includes these db values. This is done as follows.
```
python initenv.py
```
Activate the .env file by sourcing it
```
source .env
```
Test if it is working by running in bash
```
echo $SECRET_KEY
```

#### Migrating the database for your local setup
In order to create all the tables and other structures in your project database, we should run a migration in the virtualenv local installation.	For this the user should have a local instance of postgres on their machine, he should have configured the user, db and password in this instance and the values should be added to the .env file.

```
python manage.py migrate
```
#### Running the server
After following through all the above instructions, in order to check if the local installation is working fine, we will check if it is working properly by running the light weight server bundled with django.

```
python manage.py runserver
```
If it succesfully executes your local installation is complete and good to go. If it throws an error, there is some issue with the setup. If you are unabe to debug it, contact me.

## Resources followed

1. [Philosophy](https://www.b-list.org/weblog/2008/mar/15/slides/)
2. [Server installation details](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04)
3. [Angular Commit Details](https://github.com/angular/angular/blob/master/CONTRIBUTING.md)
