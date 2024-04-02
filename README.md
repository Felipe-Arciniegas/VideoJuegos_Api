# API VideoJuegos

API Desarrollada para la Gestion de un catalogo de videojuegos para una industria o comercio de juegos electronicos. La API le permitira visualizar el catalogo de videojuegos, tambien le permitira añadir nuevos videojuegos y editarlos despues de haberlos guardado, por ultimo tambien podra eliminar estos.

## ¿Como correr el proyecto?
**1:** Clonar el repositorio con el comando de git:
```bash
git clone <dirección del repo>
```
**2:** Ingresar desde la terminal dentro de la carpeta del proyecto. Ejemplo en linux:
```bash
cd <nombre del directorio>
```
**3:** Crear un entorno virtual:
```bash
python -m venv venv
```
**4:** Ingresar en el entorno virtual:
- Para linux y Mac:
```bash
source venv/bin/activate
```
- Para Window:
```bash
venv\Scripts\activate.bat
```
**5:** Descargar las dependencias del archivo 'requirements.txt' con el comando:
```bash
pip install -r requirements.txt   
```
**6:** Correr el servidor web de uvicorn:
```bash
uvicorn <nombre del archivo principal>:<nombre de la instancia de FastAPI> --reload
```
*ejemplo:*
```bash
uvicorn main:app --reload
```
**7:** En el navegador ir al localhost:8000.


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