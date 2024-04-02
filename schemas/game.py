from pydantic import BaseModel, Field
from typing import Optional

class Game(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=2, max_length=200)
    overview: str = Field(min_length=20, max_length=350)
    price: float = Field(ge=0.0)
    release_date: int = Field(ge=1970, le=2024)
    rating: float = Field(ge=0.0, le=10.0)
    category: str = Field(min_length=5, max_length=20)
    developer: str = Field(min_length=5, max_length=20)
    publisher: str = Field(min_length=5, max_length=20)
    
    class Config:
        model_config = {
        "json_schema_extra": {
                "examples": [
                    {
                        "id": 1,
                        "title": "Mi Juego",
                        "overview": "Descripcion del juego",
                        "price": 100.0,
                        "release_date": 2022,
                        "rating": 9.9,
                        "category": "Shooter",
                        "developer": "Desarrollador",
                        "publisher": "Editor"
                    }
                ]
            }
        }