# API VideoJuegos

API Desarrollada para la Gestion de un catalogo de videojuegos para una industria o comercio de juegos electronicos. La API le permitira visualizar el catalogo de videojuegos, tambien le permitira añadir nuevos videojuegos y editarlos despues de haberlos guardado, por ultimo tambien podra eliminar estos.

## Instalación

Para la instalacion de la API, baje los archivos del repositorio y despues simplemente ejecute:

```bash
pip install "__requirement__"
```
los programas que debe instalar se encuentran en el archivo: requierements.txt

## Uso

Para utilizar la Api debe conectar su servidor con el archivo main.py, por ejemplo:

```bash
uvicorn main:app --reload
```

## Endpoints

- `/games`: Podra visualizar el catalogo de Videojuegos agregados a la base de Datos.
- `/games/{id}`: Podra Buscar un Videojuego que se encuentre en la base de Datos por medio de su ID.
- `/games/{title}`:Podra Buscar un Videojuego que se encuentre en la base de Datos por medio de su titulo.
- `/games/login`: Autenticacion segura

## Ejemplos de Código

```python
# Ejemplo de código en Python para utilizar la API
import requests

url = 'URL_DEL_ENDPOINT'
response = requests.get(url)
data = response.json()
print(data)
```
## Documentacion Completa

Para visualizar la Documentacion completa ingrese a los siguientes Endpoints:

- `/Docs`:  Este término simplemente se refiere a la documentación de la API en general.
- `/redoc` herramienta específica para generar documentación interactiva de API's. Redoc toma un documento de especificación de API en un formato como OpenAPI (anteriormente conocido como Swagger) o RAML y lo convierte en una documentación web interactiva que los desarrolladores pueden explorar.