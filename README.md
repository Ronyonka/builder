# Builder

#### Date of Current Version (March 3rd, 2020)
#### By **Ron Onyonka**
This is a project, built on django, that allows home builders to track the flow of materials on a building site.
### Technologies Used

- HTML & CSS
- Bootstrap4
- Python
- Heroku

## Link to Live Website 
Here is a link to the live website: <https://evening-lowlands-22187.herokuapp.com/>
## Usage

The project requires a user to register/login to be able to use it.\
The default login credentials are:\
\
**Username:** **demo**\
**Passoword:** **account2020**\
\
The user can then log in items that come to the building site Selecting their names, entering the quantity and the date and time they arrived.\
They will be able to see this in the *'logs'* tab

## Setup/Installation
### Prerequisites
You need the following to work on the project: -
* Python version 3+
* Pip 
* venv 
* postgres
* git
* heroku cli

### Installation
Clone the repository and navigate into it
```bash
git clone https://github.com/Ronyonka/builder
cd builder
```

Create and activate the virtual environment

```bash
python3.6 -m venv venv
[linux & MacOs] source venv/bin/activate
[windows] venv\scripts\activate
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements

```bash
pip install -r requirements
```
Create a database

```bash
psql -U postgres
    postgres=# CREATE DATABASE inuua;
```
This assumes you are using the default postgres user, if you have different user configurations you can edit them in settings.py
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'inuua',
        'USER': 'username',#insert your postgres username here
        'PASSWORD': 'password',#insert your postgres password here
        'HOST': '127.0.0.1',
        'PORT': ''
    }
}
```

Finally make migrations
```bash
python manage.py migrate
```
Running the project
```bash
python manage.py runserver
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)