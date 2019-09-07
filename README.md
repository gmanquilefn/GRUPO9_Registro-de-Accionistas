# Administrador de Registros de Accionistas
Proyecto universitario llevado a cabo en Django.

## Dependencies
```text
django
djangorestframework
gunicorn
psycopg2
```

## Usage
Prerequisites:
```text
Docker and docker-compose needed
```

Run:
```docker-compose
docker-compose run web python manage.py migrate
docker-compose run web python manage.py createsuperuser
docker-compose up
```

## Authors
* **Pedro Conejera** - *2019* - [PedroConejera](https://github.com/PedroConejera)
* **Gonzalo Manquilef** - *2019* - [Noygan](https://github.com/Noygan)
* **Ronaldo Cavero** - *2019* - [Jcvron](https://github.com/jcvron)
* **Francisco Vargas** - *2019* - [Tostin](https://github.com/Tostin)
* **Agustín Sepúlveda** - *2019* - [Dreeakonee](https://github.com/Dreeakonee)
* **Oscar Edding** - *2019* - [OscarEdding](https://github.com/OscarEdding)
