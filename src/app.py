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
from models import db, User, Characters, Planets, Starships, FavoritesCharacters, FavoritesPlanets, FavoritesStarships
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
def handle_characters():

    characters = Characters.query.all()
    serialized_characters = [character.serialize() for character in characters]

    response_body = {
        "characters": serialized_characters,
        "msg": "Hello, this is your GET /Characters response "
        
    }

    # response_body = {
    #     "msg": "Hello, this is your GET /Characters response "
    # }

    return jsonify(response_body), 200


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

@app.route('/starships', methods=['GET'])
def handle_starships():

    starships = Starships.query.all()
    serialized_starships = [starship.serialize() for starship in starships]

    response_body = {
        "starships": serialized_starships,
        "msg": "Hello, this is your GET /Starships response "
    }
    # response_body = {
    #     "msg": "Hello, this is your GET /Starships response "
    # }

    return jsonify(response_body), 200

@app.route('/favorites/characters', methods=['GET'])
def handle_favorites_characters():

    response_body = {
        "msg": "Hello, this is your GET /Favorites Characters response "
    }

    return jsonify(response_body), 200



@app.route('/favorites/planets', methods=['GET'])
def handle_favorites_planets():

    response_body = {
        "msg": "Hello, this is your GET /Favorites Planets response "
    }

    return jsonify(response_body), 200



@app.route('/favorites/starships', methods=['GET'])
def handle_favorites_starships():

    response_body = {
        "msg": "Hello, this is your GET /Favorites Starships response "
    }

    return jsonify(response_body), 200



# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
