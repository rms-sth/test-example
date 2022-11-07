# Mero Crore

## DIRECTORY STRUCTURE

* core - core management apps of **CRORE**
* CRORE - Django project and settings

### SETTING UP DEVELOPMENT ENVIRONMENT

```shell
python3 -m venv ./venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
npm install
```

### MIGRATION

* To create migration file
  
  ```shell
  python manage.py makemigrations
  ```
  
* To migrate migration file
  
  ```shell
  python manage.py migrate
  ```

* To run application
  
  ```shell
  python manage.py runserver
  ```

### Imports

```shell
python manage.py import_dummy
python manage.py query -p ramesh
```

### APPLICATION DEPENDENCIES MODULE

* Django 4.1.x
* Python 3.10.x

#### STARTING SERVERS

* To run application server:
  
  ```shell
  python manage.py runserver
  ```
# test-example
