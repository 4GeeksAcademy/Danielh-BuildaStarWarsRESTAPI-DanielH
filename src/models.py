from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Characters(db.Model):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    height = Column(Integer)
    mass = Column(Integer)
    hair_color = Column(String(20))
    skin_color = Column(String(20))
    eye_color = Column(String(20))
    birth_year = Column(String(20))
    gender = Column(String(20))
    created = Column(String(30))
    edited = Column(String(30))
    name = Column(String(20), nullable=False)
    homeworld = Column(String(20))
    url = Column(String(20))

    def __repr__(self):
        return '<Character id={self.id}, name={self.name}>'

    def serialize(self):
        return {
            "id": self.id,
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
            "gender": self.gender,
            "created": self.created,
            "edited": self.edited,
            "name": self.name,
            "homeworld": self.homeworld,
            "url": self.url
        }


class Planets(db.Model):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    diameter = Column(Integer)
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    gravity = Column(String(20))
    population = Column(Integer)
    climate = Column(String(20))
    terrain = Column(String(20))
    surface_water = Column(Integer)
    created = Column(String(20))
    edited = Column(String(20))
    name = Column(String(20))
    url = Column(String(20))

    def __repr__(self):
        return '<Planets id={self.id}, name={self.name}>'

    def serialize(self):
        return {
            "id": self.id,
            "diameter": self.diameter,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "gravity": self.gravity,
            "population": self.population,
            "climate": self.climate,
            "terrain": self.terrain,
            "surface_water": self.surface_water,
            "created": self.created,
            "edited": self.edited,
            "name": self.name,
            "url": self.url
        }


class Starships(db.Model):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)
    model = Column(String(20))
    starship_class = Column(String(20))
    manufacturer = Column(String(20))
    cost_in_credits = Column(Integer)
    length = Column(Integer)
    crew = Column(Integer)
    passengers = Column(Integer)
    max_atmosphering_speed = Column(Integer)
    hyperdrive_rating = Column(Integer)
    MGLT = Column(Integer)
    cargo_capacity = Column(Integer)
    consumables = Column(String(20))
    pilots = Column(String(20))
    created = Column(String(25))
    edited = Column(String(250))
    name = Column(String(20))
    url = Column(String(250))

    def __repr__(self):
        return '<Starships id={self.id}, name={self.name}>'

    def serialize(self):
        return {
            "id": self.id,
            "model": self.model,
            "starship_class": self.starship_class,
            "manufacturer": self.manufacturer,
            "cost_in_credits": self.cost_in_credits,
            "length": self.length,
            "crew": self.crew,
            "passengers": self.passengers,
            "max_atmosphering_speed": self.max_atmosphering_speed,
            "hyperdrive_rating": self.hyperdrive_rating,
            "MGLT": self.MGLT,
            "cargo_capacity": self.cargo_capacity,
            "consumables": self.consumables,
            "pilots": self.pilots,
            "created": self.created,
            "edited": self.edited,
            "created": self.created,
            "name": self.name,
            "url": self.url
        }


class Favorites(db.Model):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    characters_id = Column(Integer, ForeignKey('characters.id'))
    characters = relationship(Characters)
    planets_id = Column(Integer, ForeignKey('planets.id'))
    planets = relationship(Planets)
    starships_id = Column(Integer, ForeignKey('starships.id'))
    starships = relationship(Starships)

    def __repr__(self):
        return '<Favorites id={self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "characters_id": self.characters_id,
            "planets_id": self.planets_id,
            "starships_id": self.starships_id,
            
        }
