from typing import List
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Path, Query, Depends

from schemas.game_schema import Game
from config.databaseV import Session
from models.game_model import Game as GameModel
from services.game_service import GameService
from middlewares.jwt_bearer import JWTBearer

games_router = APIRouter()

@games_router.get("/games", tags=['games'], response_model=List[Game], status_code=200)
def get_games() -> List[Game]:
    db = Session()
    result = GameService(db).get_games()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

#Segundo End Point
@games_router.get("/games/{id}", tags=['games'], response_model=Game, status_code=200)
def get_game(id: int = Path(ge=1, le=2000)) -> Game:
    db = Session()
    result = GameService(db).get_game(id)
    if result:
        result = JSONResponse(content=jsonable_encoder(result), status_code=200)
    else:
        result = JSONResponse(content={"message": "Game not found"}, status_code=404)
    return result

#Tercer End Point
@games_router.get("/games/", tags=['games'], response_model=List[Game])
def get_games_by_category(category: str = Query(min_length=3, max_length=15)) -> List[Game]:
    db = Session()
    result = GameService(db).get_games_by_category(category)
    if result:
        result = JSONResponse(content=jsonable_encoder(result), status_code=200)
    else:
        result = JSONResponse(content={"message": "Game not found"}, status_code=404)
    return result

#Cuarto End Point
@games_router.post("/games", tags=['games'], response_model=dict, status_code=201)
def create_game(game: Game) -> dict:
    db = Session()
    GameService(db).create_game(game)
    return JSONResponse(content={"message": "Game created successfully"}, status_code=201)

@games_router.put("/games/{id}", tags=['games'], response_model=dict, status_code=200)
def update_game(id: int, game: Game) -> dict:
    db = Session()
    game = GameService(db).get_game(id)
    if not game:
        response = JSONResponse(content={"message": "Game not found"}, status_code=404)
    else:
        GameService(db).update_game(game)
        response = JSONResponse(content={"message": "Game updated successfully"}, status_code=200)
    return response

@games_router.delete("/games/{id}", tags=['games'], response_model=dict, dependencies=[Depends(JWTBearer())])
def delete_game(id: int) -> dict:
    db = Session()
    game = GameService(db).get_game(id)
    if not game:
        response = JSONResponse(content={"message": "Game not found"}, status_code=404)
    else:
        GameService(db).delete_game(game)
        response = JSONResponse(content={"message": "Game deleted successfully"}, status_code=200)
    return response

#Quinto End Point
@games_router.get("/games/", tags=['games'], response_model=List[Game])
def get_games_by_developer(developer: str = Query(min_length=3, max_length=15)) -> List[Game]:
    db = Session()
    result = GameService(db).get_games_by_developer(developer)
    if result:
        result = JSONResponse(content=jsonable_encoder(result), status_code=200)
    else:
        result = JSONResponse(content={"message": "Game not found"}, status_code=404)
    return result

#Sexto End Point
@games_router.get("/games/", tags=['games'], response_model=List[Game])
def get_games_by_publisher(publisher: str = Query(min_length=3, max_length=15)) -> List[Game]:
    db = Session()
    result = GameService(db).get_games_by_publisher(publisher)
    if result:
        result = JSONResponse(content=jsonable_encoder(result), status_code=200)
    else:
        result = JSONResponse(content={"message": "Game not found"}, status_code=404)
    return result


#Octavo End Point
@games_router.get("/games/", tags=['games'], response_model=List[Game])
def get_games_by_release_date(release_date: int = Query(ge=1970, le=2021)) -> List[Game]:
    db = Session()
    result = GameService(db).get_games_by_release_date(release_date)
    if result:
        result = JSONResponse(content=jsonable_encoder(result), status_code=200)
    else:
        result = JSONResponse(content={"message": "Game not found"}, status_code=404)
    return result

#Noveno End Point
@games_router.get("/games/", tags=['games'], response_model=List[Game])
def get_games_by_title(title: str = Query(min_length=3, max_length=50)) -> List[Game]:
    db = Session()
    result = GameService(db).get_games_by_title(title)
    if result:
        result = JSONResponse(content=jsonable_encoder(result), status_code=200)
    else:
        result = JSONResponse(content={"message": "Game not found"}, status_code=404)
    return result