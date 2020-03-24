from ..engine_base.base_engine import Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

class Artist(Base):
    __tablename__ = 'artists'
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)
    Album = relationship("Album")

    def __init__(self, Name):
        self.Name = Name

class Album(Base):
    __tablename__ = 'albums'
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey('artists.ArtistId'))
    Artist = relationship("Artist")

    def __init__(self, Title, Artist):
        self.Title = Title
        self.Artist = Artist
