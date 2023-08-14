import os
from flask_admin import Admin
from models import db, User, Characters, Planets, Starships, FavoritesCharacters, FavoritesPlanets, FavoritesStarships, Person
from flask_admin.contrib.sqla import ModelView
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='4Geeks Admin', template_mode='bootstrap3')

    
    # Add your models here, for example this is how we add a the User model to the admin
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Characters, db.session))
    admin.add_view(ModelView(Planets, db.session))
    admin.add_view(ModelView(Starships, db.session))
    admin.add_view(ModelView(FavoritesCharacters, db.session))
    admin.add_view(ModelView(FavoritesPlanets, db.session))
    admin.add_view(ModelView(FavoritesStarships, db.session))
    admin.add_view(ModelView(Person, db.session))
    





    # You can duplicate that line to add mew models
    # admin.add_view(ModelView(YourModelName, db.session))