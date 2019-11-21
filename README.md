# Administrador de Registros de Accionistas
Proyecto universitario llevado a cabo en Django.

[Demo en Heroku >>](https://registro-accionistas.herokuapp.com/)

* Usuario de prueba: 
  * Nombre de Usuario: `root`
  * Contraseña: `root`

[Tablero del Proyecto en Trello >>](https://trello.com/b/BP7z3o5H/grupo9registro-de-accionistas)

## Dependencies 📋
* Docker:
  ```Docker
    sudo apt install docker-compose
  ```
  * [Docker installation](https://docs.docker.com/install/)
  * [Docker-compose installation](https://docs.docker.com/compose/install/)

## Usage 🚀
>To run django server:
  ```docker-compose
  docker-compose build
  docker-compose run web python manage.py makemigrations
  docker-compose run web python manage.py migrate
  docker-compose run web python manage.py createsuperuser
  docker-compose up
  ```

>Reset db:
  ```docker-compose
  docker-compose stop
  docker rm grupo9registrodeaccionistas_db_1
  ```

>Stop containers, networks and drop database:
  ```Docker
  docker-compose run web rails db:drop
  docker-compose stop
  docker-compose down
  ```

>Delete images, containers, build cache and networks
  ```Docker
  docker rmi $(docker images -q)
  docker rm $(docker ps -a -q)
  docker system prune
  ```

## Known Issues 📢
1) To fix **"ERROR: for grupo9registrodeaccionistas_db_1  Cannot start service db: driver failed programming external connectivity on endpoint grupo9registrodeaccionistas_db_1 (8ca475d599099affea877a2b4e3cd19eaca4d31bd26120f8f85ea699b644fccd): Error starting userland proxy: listen tcp 0.0.0.0:5432: bind: address already in use"** :
    ```Fix
      sudo service postgresql stop
    ```

## Authors ✒️
* **Pedro Conejera** - *2019* - [PedroConejera](https://github.com/PedroConejera)
* **Gonzalo Manquilef** - *2019* - [GonzaloManquilef](https://github.com/GonzaloManquilef)
* **Ronaldo Cavero** - *2019* - [Jcvron](https://github.com/jcvron)
* **Francisco Vargas** - *2019* - [Tostin](https://github.com/Tostin)
* **Agustín Sepúlveda** - *2019* - [Dreeakonee](https://github.com/Dreeakonee)
* **Oscar Edding** - *2019* - [OscarEdding](https://github.com/OscarEdding)
