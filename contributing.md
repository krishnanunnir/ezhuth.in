# Contributing to KNODE	

## How to run local version?

A local copy of the website can be very easily run. For this create a virtual environment using python3, and install the dependencies for the site using the requirements.txt file. Add an environment settings file from which database data, allowed hosts, secret key and debug value is imported by the settings file. These steps are explained in further detail below.

## Commiting

We will be using the angular style of commits <sup>[3](https://github.com/angular/angular/blob/master/CONTRIBUTING.md)</sup>, modified accordingly for our project. Please refer past commits to get an idea


## Setting up local environment settings and running local build	We will be using the angular style of commits, modified accordingly for our project. 


This will walk you through setting up the local environment settings file(env_setting.py) and setting up the local build of the website.	# Resources followed


#### Generating secret key for your local environment settings files
  
The security key for a project is used for encrypting the project, therefore it is important to keep it a secret. Therefore each user should generate and add their own secret key which is to be added to the environment settings file. For more info check [here](https://stackoverflow.com/questions/4664724/distributing-django-projects-with-unique-secret-keys)	 

#### Configuring the database	

This project uses PostgreSQL as its database management system. We will be using the psycopg database adapter for connecting the Django models to the database. Create your own user and database in postgres for running the project <sup>[2](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04)</sup>.Copy the following code to your environment setting file  (env_setting.py).	

```	
DATABASES = {	
    'default': {	
        'ENGINE': 'django.db.backends.postgresql_psycopg2',	
        'NAME': 'myproject',	
        'USER': 'myprojectuser',	
        'PASSWORD': 'password',	
        'HOST': 'localhost',	
        'PORT': '',	
    }	
}	
```	
Replace the different values with values of user and db created by you. After replacing the values, migrate your code by running.	

```	
python manage.py migrate	
```	

#### Further changes in local environment settings file	

Since we will be running the python on our local machine add localhost to 'ALLOWED_HOSTS'. Furthermore set debug to true as we will be debugging it here. The final environment settings file should have the following.	

```	
ALLOWED_HOSTS = ['127.0.0.1']	
DEBUG = True	
DATABASES = {<database-settings>}	
SECRET_KEY = '<secret-key-value>'	
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