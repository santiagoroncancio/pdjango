# pdjango
Proyecto del curso  aplicaciones web con django de codigofacilito 

- django 3.0.6
- bootstrap

# Estrutura
- Modelo —> Base de datos
- Template —> Capa de presentación 
- Vistas —> Lógica del negocio

## Comandos basicos 
- Crear entorno virtual	--> python3 -m vena env
- activar el entorno virtual --> source env/bin/activate
- iniciar un proyecto --> django-admin startproject nombre
- Correr server --> Python3 manage.py runserver
- Migración --> Python3 manage.py migrate
- Hacer una migracion --> Python3 manage.py makemigrations
- Crear usuario	--> Python3 manage.py createsuperuser

- Iniciar una aplicación --> Python3 manage.py startalp nombre
- Shell interactiva --> python3 manage.py shell
- Uso de imagenes --> Pip install pillow

## Respaldo de la informacion 
- python3 manage.py dumpdata products.product --format=json --indent=4 > products/fixtures/products.json

## restaurar informacion
- python3 manage.py loaddata products.json
