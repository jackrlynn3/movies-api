from dataclasses import dataclass

# Character: class used to describe characters in movies
@dataclass
class Character:
    name : str
    height : int
    mass : float
    hair_color : str
    skin_color : str
    eye_color : str
    birth_year : int
    gender : str

    # Docstring
    """
    Character
    --------
    name: str
    height: int
    mass: float
    hair_color: str
    skin_color: str
    eye_color: str
    birth_year: int
    gender: str
    --------
    """