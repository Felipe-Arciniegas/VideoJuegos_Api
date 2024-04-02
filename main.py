from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from config.databaseV import  engine, Base
from routers.game_router import games_router
from routers.auth_router import auth_router

# Creando una instancia de la clase FastAPI
app = FastAPI()
Base.metadata.create_all(bind=engine)

# Cambios a la documentacion
app.title = "VideoGames Api"
app.version = "V1.0.0"
app.include_router(games_router)
app.include_router(auth_router)

#Primer End Point
@app.get("/", tags=["Home"])
def message():
    return HTMLResponse(
        content="<h1>Bienvenido a mi Super Api (VideoJuegos)</h1>"
    )