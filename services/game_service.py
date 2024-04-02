from schemas.game_schema import Game
from models.game_model import Game as GameModel

class GameService():
    def __init__(self, db):
        self.db = db

    def get_games(self):
        return self.db.query(GameModel).all()

    def get_game(self, id:int):
        return self.db.query(GameModel).filter(GameModel.id == id).first()
    
    def get_games_by_category(self, category:str):
        return self.db.query(GameModel).filter(GameModel.category == category).all()
    
    def create_game(self, game:Game):
        new_game = GameModel(**game.model_dump())
        self.db.add(new_game)
        self.db.commit()

    def update_game(self, game: GameModel, data:Game):
        game.title = data.title
        game.overview = data.overview
        game.price = data.price
        game.release_date = data.release_date
        game.rating = data.rating
        game.category = data.category
        game.developer = data.developer
        game.publisher = data.publisher
        self.db.commit()

    def delete_game(self, game: GameModel):
        self.db.delete(game)
        self.db.commit()