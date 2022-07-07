# Import statements
from config import api_key
import sys
sys.path.insert(1, "class/")
from Character import Character
from Media import Media
from StarWarsLib import StarWarsLib
import os
import requests
import json

def getCharacters():

    characters = []

    # Connect to get Star Wars characters
    for page in range(1, 10):
        json_int = requests.get(f'https://swapi.dev/api/people/?page={page}')
        
        # Get json text
        character_data = json.loads(json_int.text)['results']
        for character in character_data:

            # Get name as str
            name = character['name']

            # Try to get height as int but use None if not possible
            try:
                height = int(character['height'])
            except:
                height = None

            # Try to get mass as int but use None if not possible
            try:
                mass = int(character['mass'])
            except:
                mass = None
            
            # Get hair color as str
            hair_color = character['hair_color']

            # Get skin color as str
            skin_color = character['skin_color']

            # Get eye color as str
            eye_color = character['eye_color']

            # Get birth year as float but use None if not possible
            try:
                birth_year = float(character['birth_year'].strip('BBY'))
            except:
                birth_year = None

            # Get gender as string
            gender = character['gender']

            # Create character object
            this_character = Character(name, height, mass, hair_color, skin_color, eye_color, birth_year, gender)

            # Get movies that this character is in
            movies = []
            movies_full = character['films']
            for movie in movies_full:
                movies.append(int(movie.strip('https://swapi.dev/api/films/').strip('/')))

            # Add this to character global variable
            characters.append({'name': name, 'character': this_character, 'movies': movies})
    
    return characters

def main():

    # Get characters data
    characters = getCharacters()


main()