# Administrador de Registros de Accionistas
Proyecto universitario llevado a cabo en Django.

## Dependencies
Create _**requirements.txt**_ inside regAccionistas folder and put the text below
```text
django
djangorestframework
gunicorn
```

## Usage
Installation:
```shell
pip3 install -r requirements.txt
pip3 install virtualenv
virtualenv venv
cd venv/Scripts/
activate.bat
```

Run:
```python
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Authors
* **Pedro Conejera** - *2019* - [PedroConejera](https://github.com/PedroConejera)
* **Gonzalo Manquilef** - *2019* - [Noygan](https://github.com/Noygan)
* **Ronaldo Cavero** - *2019* - [Jcvron](https://github.com/jcvron)
* **Francisco Vargas** - *2019* - [Tostin](https://github.com/Tostin)
* **Agustín Sepúlveda** - *2019* - [Dreeakonee](https://github.com/Dreeakonee)
