"""CRUD operations."""


from model import db, connect_to_db, Wine, Cheese


def create_wine(wine_name, wine_pronunciation, wine_color, wine_sparkling, 
                wine_region, wine_country, wine_bio, wine_img, wine_sub):
    """Create and return a wine."""

    wine = Wine(wine_name=wine_name,
                wine_pronunciation=wine_pronunciation,
                wine_color=wine_color,
                wine_sparkling=wine_sparkling,
                wine_region=wine_region,
                wine_country=wine_country,
                wine_bio=wine_bio,
                wine_img=wine_img,
                wine_sub=wine_sub)

    db.session.add(wine)
    db.session.commit()

    return wine


def create_cheese(cheese_name, cheese_pronunciation, cheese_region, cheese_density, 
                    cheese_description, cheese_bio, cheese_animal, cheese_img, 
                    cheese_sub):
    """Create and return a cheese."""

    cheese = Cheese(cheese_name=cheese_name, cheese_pronunciation=cheese_pronunciation, 
                    cheese_region=cheese_region, cheese_density=cheese_density, 
                    cheese_description=cheese_description, cheese_bio=cheese_bio,
                    cheese_animal=cheese_animal, cheese_img=cheese_img, 
                    cheese_sub=cheese_sub)

    db.session.add(cheese)
    db.session.commit()

    return cheese


if __name__ == '__main__':
    from server import app
    connect_to_db(app)