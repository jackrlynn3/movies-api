from dataclasses import dataclass
from datetime import datetime

# StarWarsLib: Class that holds all stars wars movies and shows
@dataclass
class StarWarsLib:
    movies : list()
    shows : list()
    last_updated : datetime

    # Docstring
    """
    StarWarsLib
    --------
    + movies: list(Media)
    + shows: list(media)
    + last_updated: datetime
    --------
    + add_movie(Media)
    + add_show(Media)
    """

    def add_movie(self, media):
        self.movies.append(media)
    
    def add_show(self, media):
        self.shows.append(media)