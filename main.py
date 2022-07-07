# Import statements
from matplotlib.pyplot import plot
from config import api_key
import sys
sys.path.insert(1, "class/")
from Character import Character
from Media import Media
from StarWarsLib import StarWarsLib
import os
import requests
import json
from datetime import datetime

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

def getMovies():

    movies = []

    # Get all character data
    characters = getCharacters()

    # First load SWAPI API stuff
    json_int_swapi = requests.get(f'https://swapi.dev/api/films')
    swapi_data = json.loads(json_int_swapi.text)['results']
    for movie in swapi_data:

        # Get all direct data
        title = movie['title']
        episode_id = int(movie['episode_id'])
        opening_crawl = movie['opening_crawl']
        director = movie['director']
        producer = movie['producer']
        release_date = datetime.strptime(movie['release_date'], '%Y-%m-%d').date()
        
        # Get characters indirectly
        this_characters = []
        for character in characters:
            if episode_id in character['movies']:
                this_characters.append(character['character'])
        
        # Get this movies instance of OMDb
        json_int_omdb = requests.get(f'http://www.omdbapi.com/?apikey={api_key}&t={title}')
        omdb_data = json.loads(json_int_omdb.text)
        plot = omdb_data['Plot']
        tomatometer_score = 0
        for rating in omdb_data['Ratings']:
            if rating['Source'] == 'Rotten Tomatoes':
                tomatometer_score = int(rating['Value'].replace('%', ''))
        try:
            box_office_gross = int(omdb_data['BoxOffice'].replace(',', '').replace('$', ''))
        except:
            box_office_gross = None

        # Create a media instance
        this_media = Media(title, episode_id, opening_crawl, director, producer, release_date, this_characters, plot, tomatometer_score, box_office_gross)

        # Add to movies list
        movies.append(this_media)

    # Return movies
    return(movies)

def main():

    movies = getMovies()
    for movie in movies:
        print(movie.plot)
        print(movie.tomatometer_score)
        print(movie.box_office_gross)
    #getMovies()


main()