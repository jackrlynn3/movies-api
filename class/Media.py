from dataclasses import dataclass, field
import datetime

# Media: class used to describe Star Wars movies
@dataclass
class Media:
    title : str
    episode_id : int
    opening_crawl : str
    director : str
    producer : str
    release_date : datetime = field(metadata={'units':'CE'})
    characters : list()
    plot : str
    tomatometer_score : float = field(metadata={'units':'Tomatometer percentile'})
    box_office_gross : float = field(metadata={'units':'millions of USD'})

    # Docstring
    """
    Media
    --------
    + title: str
    + episode_id: int
    + opening_crawl: str
    + director: str
    + producer: str
    + release_date: datetime
    + characters: list(str)
    + plot: str
    + tomatometer_score: float
    + box_office_gross: float
    --------
    + add_character(Character)
    """

    # Add character method
    def add_character(self, character):
        self.characters.append(character)