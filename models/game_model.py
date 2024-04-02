from config.databaseV import Base
from sqlalchemy import Column, Integer, String, Float

class Game(Base):
    __tablename__ = "games"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), unique=True, index=True, nullable=False)
    overview = Column(String(350), nullable=False)
    price = Column(Float, nullable=False)
    release_date = Column(Integer, nullable=False)
    rating = Column(Float, nullable=False)
    category = Column(String(20), nullable=False)
    developer = Column(String(20), nullable=False)
    publisher = Column(String(20), nullable=False)