# Administrador de Registros de Accionistas

Proyecto universitario en Django.

![](https://i.imgur.com/FnBMhZZ.jpg?1)

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
[Pedro Conejera](https://github.com/PedroConejera) | 2019
[Gonzalo Manquilef](https://github.com/Noygan) | 2019
[Ronaldo Cavero](https://github.com/jcvron) | 2019
[Francisco Vargas](https://github.com/Tostin) | 2019
[Agustín Sepúlveda](https://github.com/Dreeakonee) | 2019