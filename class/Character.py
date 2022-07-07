from dataclasses import dataclass, field

# Character: class used to describe characters in movies
@dataclass
class Character:
    name : str
    height : int = field(metadata={'units':'cm'})
    mass : int = field(metadata={'units':'kg'})
    hair_color : str
    skin_color : str
    eye_color : str
    birth_year : float = field(metadata={'units':'BBY'})
    gender : str

    # Docstring
    """
    Character
    --------
    + name: str
    + height: int
    + mass: int
    + hair_color: str
    + skin_color: str
    + eye_color: str
    + birth_year: float
    + gender: str
    --------
    """