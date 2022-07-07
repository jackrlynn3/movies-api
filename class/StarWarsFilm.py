
from dataclasses import dataclass
from datetime import datetime

# StarWarsFilm: class used to describe Star Wars movies
@dataclass
class StarWarsFilm:
    title : str
    episode_id : int
    opening_crawl : str
    director : str
    producer : str
    release_date : datetime
    characters : list()
    plot : str
    tomatometer_score : float
    box_office_gross : float

    # Docstring
    """
    StarWarsFilm
    --------
    title: str
    episode_id: int
    opening_crawl: str
    director: str
    producer: str
    release_date: datetime
    characters: list(str)
    plot: str
    tomatometer_score: float
    box_office_gross: float
    --------
    add_character(Character)
    """

    # Add character method
    def add_character(self, character):
        self.characters.append(character)