# KNODE	

## django forum builder or KNODE

KNODE is an easy to install forum builder where users can easily setup a new forum in less than 5 minutes. Future releases will include an option to use this as a blog.

## Commiting

We will be using the angular style of commits <sup>[3](https://github.com/angular/angular/blob/master/CONTRIBUTING.md)</sup>, modified accordingly for our project. Please refer past commits to get an idea

## Running a build on your machine

This will walk you through the process of running this website locally on your machine. For ease of usage we have two settings file settings/local.py and settings/production.py, we will be using the local.py file for running our local build. We need to configure our machine details mainly databse in the local.py

#### Configuring the database	

This project uses PostgreSQL as its database management system. We will be using the psycopg database adapter for connecting the Django models to the database. Create your own user and database in postgres for running the project <sup>[2](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04)</sup>. Set the values for the various database parameters in the local/settings.py.

```	
SECRET_KEY = '*vul$9+^oao+-c)iv75q(urt*-_^olp2)&8r0gvg$7xfw4px+g'
ALLOWED_HOSTS = ['127.0.0.1','herokapp.com']
DEBUG = True
DATABASE_ENGINE = 'django.db.backends.postgresql_psycopg2'
DATABASE_NAME = 'knodev'
DATABASE_USER = 'postgres'
DATABASE_PASSWORD = '123456789'
DATABASE_HOST = 'localhost'
DATABASE_PORT = ''
```	
Replace the default values with values of user and db created by you.

#### Other changes in local settings file	

By default the æALLOWED_HOSTS' is set to the local host value and 'DEBUG' is set to True, these parameters can be changed

```	
ALLOWED_HOSTS = ['127.0.0.1']	
DEBUG = True	
```	

#### Setting up local installation of the Project	
 After the above changes have been made, we will setup the local environment for the project. Create a python virtual environment to deal with dependencies. 	

 ```	
 cd /path-to-projectdir/	
 python3 -m venv <venv-folder-name>	
 ```	
After creating the virtual environment we need to activate it.	

```	
source ./<venv-folder-name>/bin/activate	
```	
After activating the virtual environment we need to install the dependencies for the project, which can be done as follows.	
```	
pip install -r requirements.txt	
```	
#### Migrating the database for your local setup	
In order to create all the tables and other structures in your project database, we should run a migration in the virtualenv local installation.	

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
