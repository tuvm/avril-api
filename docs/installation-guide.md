### Install required packages:

```bash
$ pip install -r requirements/local.txt
```

### Install MySQL

```bash
$ pip install mysqlclient
```

### Migrate database

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

### Run local

```bash
$ python manage.py runserver
```

### Fix Visual studio Code linter warning

```bash
$ pip install pylint-django
```
Then in Visual Studio Code goto: User Settings (<kbd>Ctrl</kbd> + <kbd>,</kbd> or File > Preferences > Settings if available ) Put in the following (please note the curly braces which are required for custom user settings in VSC):

```
{"python.linting.pylintArgs": [
     "--load-plugins=pylint_django"
],}
```
