# Administrador de Registros de Accionistas
Proyecto universitario llevado a cabo en Django.

[Tablero del Proyecto en Trello >>](https://trello.com/b/BP7z3o5H/grupo9registro-de-accionistas)

## Dependencies
Docker:
```Docker
sudo apt install docker-compose
```
[Docker installation](https://docs.docker.com/install/)

[Docker-compose installation](https://docs.docker.com/compose/install/)

## Usage
Run:
```docker-compose
docker-compose up
docker-compose run web python manage.py makemigrations
docker-compose run web python manage.py migrate
docker-compose run web python manage.py createsuperuser
docker-compose up
```

Reset db:
```docker-compose
docker-compose stop
docker rm grupo9registrodeaccionistas_db_1
```

## Authors
* **Pedro Conejera** - *2019* - [PedroConejera](https://github.com/PedroConejera)
* **Gonzalo Manquilef** - *2019* - [GonzaloManquilef](https://github.com/GonzaloManquilef)
* **Ronaldo Cavero** - *2019* - [Jcvron](https://github.com/jcvron)
* **Francisco Vargas** - *2019* - [Tostin](https://github.com/Tostin)
* **Agustín Sepúlveda** - *2019* - [Dreeakonee](https://github.com/Dreeakonee)
* **Oscar Edding** - *2019* - [OscarEdding](https://github.com/OscarEdding)
