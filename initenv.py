from django.core.management.utils import get_random_secret_key

ALLOWED_HOSTS = input("ALLOWED_HOSTS:\t") or "['127.0.01']"
DEBUG = input("DEBUG:\t") or "False"
SECRET_KEY = get_random_secret_key()
DATABASE_NAME =input("DATABASE_NAME:\t")
DATABASE_USER =input("DATABASE_USER:\t")
DATABASE_PASSWORD =input("DATABASE_PASSWORD:\t")
DATABASE_HOST =input("DATABASE_HOST:\t")

file_write = """\
export ALLOWED_HOSTS=%s
export DEBUG=%s
export SECRET_KEY=%s
export DATABASE_NAME=%s
export DATABASE_USER=%s
export DATABASE_PASSWORD=%s
export DATABASE_HOST=%s \
""" %(ALLOWED_HOSTS, DEBUG, SECRET_KEY, DATABASE_NAME, DATABASE_USER, DATABASE_PASSWORD, DATABASE_HOST)
with open(".env",'w') as the_file:
    the_file.write(file_write)