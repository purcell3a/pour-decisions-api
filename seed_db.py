# seed script to populated pour decisions db

import os
import crud
import server

# import all model classes and functions to talk to db
from model import db, connect_to_db, Wine, Cheese
import psycopg2
import pandas as pd

from sqlalchemy import create_engine
engine = create_engine('postgresql://Loranne@localhost:5432/pourdecisions')


# drop then recreate to start db from scratch
os.system("dropdb pourdecisions")
os.system("createdb pourdecisions")

# once that's done, we connect
connect_to_db(server.app)
# and create our model classes inside the db
db.create_all()

# populate cheeses table from csv
cheese_file = open("data/cheese.csv", "r")
next(cheese_file)

for row in cheese_file:
    fields = row.split("|") 
    for field in fields:
        if field == "":
            field = None

    cheese_name, cheese_pronunciation, cheese_region, cheese_density, cheese_description, cheese_bio, cheese_animal, cheese_img, cheese_sub = fields

    crud.create_cheese(cheese_name, cheese_pronunciation, cheese_region, cheese_density, 
                        cheese_description, cheese_bio, cheese_animal, cheese_img, 
                        cheese_sub)

cheese_file.close()

# populate wines table
wine_file = open("data/wine.csv", "r")
next(wine_file)

for row in wine_file:
    fields = row.split("|") 
    # converting sparkling values to true booleans
    # have to enumerate because field in fields is just a local variable and doesn't
    # persist beyond the loop (and we have to crud.create outside the loop)
    for i, field in enumerate(fields):
        if fields[i] == "":
            fields[i] = None
        elif fields[i] == "T":
            fields[i] = True
        elif fields[i] == "F":
            fields[i] = False

    wine_name, wine_pronunciation, wine_color, wine_sparkling, wine_region, wine_country, wine_bio, wine_img, wine_sub = fields

    crud.create_wine(wine_name, wine_pronunciation, wine_color, wine_sparkling,
                        wine_region, wine_country, wine_bio, wine_img, wine_sub)

wine_file.close()



