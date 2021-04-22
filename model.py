"""Models for wine and cheese app."""

from flask_sqlalchemy import SQLAlchemy
import crud

db = SQLAlchemy()


class Wine(db.Model):
    """A wine."""

    __tablename__ = "wines"

    # make everything but name and bio nullable to include beer and sangria
    wine_id = db.Column(db.Integer,
                        primary_key=True,
                        autoincrement=True)
    wine_name = db.Column(db.String, nullable=False)
    wine_pronunciation = db.Column(db.String)
    wine_color = db.Column(db.String)
    wine_sparkling = db.Column(db.Boolean)
    wine_region = db.Column(db.String)
    wine_country = db.Column(db.String)
    wine_bio = db.Column(db.Text, nullable=False)
    wine_img = db.Column(db.String)
    wine_sub = db.Column(db.String)

    def __repr__(self):
        return f'<Wine Information wine_id={self.wine_id} wine_name={self.wine_name}>'


class Cheese(db.Model):
    """A cheese."""

    __tablename__ = "cheeses"
    
    cheese_name = db.Column(db.String, nullable=False)
    cheese_pronunciation = db.Column(db.String)
     # made nullable. not all cheeses have region listed
    cheese_region = db.Column(db.String)
     # L - made density nullable. not all cheeses have this info
    cheese_density = db.Column(db.String)
    cheese_description = db.Column(db.Text)
    cheese_bio = db.Column(db.Text, nullable=False)
    cheese_animal = db.Column(db.String)
    cheese_img = db.Column(db.String)
    # L - made desc nullable. not all cheeses have one!
    cheese_sub = db.Column(db.String)
    cheese_id = db.Column(db.Integer,
                          primary_key=True,
                          autoincrement=True,)

    def __repr__(self):
        return f'<Cheese Information cheese_id={self.cheese_id} cheese_name={self.cheese_name}>'


def connect_to_db(app):
    # Configure to use our PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pourdecisions'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == '__main__':
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    print("Connected to DB.")