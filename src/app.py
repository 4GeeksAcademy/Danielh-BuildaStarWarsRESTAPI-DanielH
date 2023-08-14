"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Characters, Planets, Starships, FavoritesCharacters, FavoritesPlanets, FavoritesStarships, Person
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

    

@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200



@app.route('/characters', methods=['GET'])
def handle_all_characters():

    characters = Characters.query.all()
    serialized_characters = [character.serialize() for character in characters]

    response_body = {
        "characters": serialized_characters,
        "msg": "Hello, esto es tu GET de todos los /Characters y responde "
        
    }

  

    return jsonify(response_body), 200



@app.route('/characters/<int:character_id>', methods=['GET'])
def get_single_character(character_id):

    character = Characters.query.get(character_id)
    if character is None:
        return "Character not found, este personaje no existe menda", 404

    return jsonify(character.serialize()), 200



@app.route('/planets', methods=['GET'])
def handle_planets():

    planets = Planets.query.all()
    serialized_planets = [planet.serialize() for planet in planets]

    response_body = {
        "planets": serialized_planets,
        "msg": "Hello, this is your GET /Planets response "
        
    }

    # response_body = {
    #     "msg": "Hello, this is your GET /Planets response "
    # }

    return jsonify(response_body), 200



@app.route('/planets/<int:planet_id>', methods=['GET'])
def get_single_planet(planet_id):

    planet = Planets.query.get(planet_id)
    if planet is None:
        return "Planet not found, este planeta no existe menda", 404

    return jsonify(planet.serialize()), 200


    
# @app.route('/starships/<int:Starships_id>', methods=['PUT', 'GET'])
# def get_single_starship(Starships_id):
#     """
#     Single person
#     """
#     body = request.get_json()  # Input: {'username': 'new_username'}
#     if request.method == 'PUT':
#         starship1 = Starships.query.get(starships_id)
#         starship1.name = body.name
#         db.session.commit()
#         return jsonify(starship1.serialize()), 200
#     if request.method == 'GET':
#         starship1 = Starships.query.get(starships_id)
#         return jsonify(starship1.serialize()), 200
#     return "Invalid Method, esto que lo que es", 404


@app.route('/starships', methods=['GET'])
def handle_all_starships():

    starships = Starships.query.all()
    serialized_starships = [starship.serialize() for starship in starships]

    response_body = {
        "starships": serialized_starships,
        "msg": "Hello, esto es el GET  de todas /Starships responde "
    }
  
    return jsonify(response_body), 200


    
@app.route('/starships/<int:starships_id>', methods=['GET'])
def get_single_starship(starships_id):

    starship = Starships.query.get(starships_id)
    if starship is None:
        return "starship not found, esta nave no existe menda", 404

    return jsonify(starship.serialize()), 200



@app.route('/favorites/characters', methods=['GET'])
def handle_favorites_characters():

    favorites_characters = FavoritesCharacters.query.all()
    serialized_characters = [character.serialize() for character in favorites_characters]

    response_body = {
        "Favorites Characters": serialized_characters,
        "msg": "Hello, this is your GET /Favorites Characters response "
    }

    return jsonify(response_body), 200



@app.route('/favorites/planets', methods=['GET'])
def handle_favorites_planets():

    favorites_planets = FavoritesPlanets.query.all()
    serialized_planets = [planets.serialize() for planet in favorites_planets]

    response_body = {
        "Favorites Planets": serialized_planets,
        "msg": "Hello, this is your GET /Favorites Characters response "
    }

    return jsonify(response_body), 200

    response_body = {
        "msg": "Hello, this is your GET /Favorites Planets response "
    }

    return jsonify(response_body), 200



@app.route('/favorites/starships', methods=['GET'])
def handle_favorites_starships():

    favorites_starships = FavoritesStarships.query.all()
    serialized_starships = [starships.serialize() for starship in favorites_starships]

    response_body = {
        "Favorites Starships": serialized_starships,
        "msg": "Hello, this is your GET /Favorites Starships response "
    }

    

    return jsonify(response_body), 200



@app.route('/person/<int:person_id>', methods=['PUT', 'GET'])
def get_single_person(person_id):
    """
    Single person
    """
    body = request.get_json()  # Input: {'username': 'new_username'}
    if request.method == 'PUT':
        user1 = Person.query.get(person_id)
        user1.username = body.username
        db.session.commit()
        return jsonify(user1.serialize()), 200
    if request.method == 'GET':
        user1 = Person.query.get(person_id)
        return jsonify(user1.serialize()), 200
    return "Invalid Method", 404



# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
