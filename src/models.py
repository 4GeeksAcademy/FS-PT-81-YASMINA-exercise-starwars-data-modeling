import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table user
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String, nullable=False)
    password =  Column(String, nullable=False)
    is_active = Column (String, nullable=False)

    favoritos = relationship("Favorito")


class Character(Base):
    __tablename__ = 'Character'
    # Here we define columns for the table Character.
    # Notice that each column is also a normal Python instance attribute.name": "Luke Skywalker",
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable = False)
    height = Column(String(250), nullable = False)
    mass = Column(String(250), nullable = False)
    skin_color = Column(String(250), nullable = False)
    eye_color = Column(String(250), nullable = False)
    birth_year = Column(String(250), nullable = False)
    gender = Column(String(250), nullable = False)
    homeworld = Column(String(250), nullable = False)
    films = Column(String(250), nullable = False)

    favoritos = relationship("Favorito")

    def to_dict(self):
        return {}
class Planet(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table planet.
    # Notice that each column is also a normal Python instance attribute.name": "Luke Skywalker",
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable = False)
    rotation_period = Column(String(250), nullable = False)
    orbital_period = Column(String(250), nullable = False)
    diameter = Column(String(250), nullable = False)
    climate = Column(String(250), nullable = False)
    gravity = Column(String(250), nullable = False)
    surface_water = Column(String(250), nullable = False)
    population = Column(String(250), nullable = False)
    residents = Column(String(250), nullable = False)

    favoritos = relationship("Favorito")

    def to_dict(self):
        return {}   
    

class Vehicle(Base):
    __tablename__ = 'vehicle'
    # Here we define columns for the table vehicle.
    # Notice that each column is also a normal Python instance attribute.name": "Luke Skywalker",
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable = False)
    model = Column(String(250), nullable = False)
    manufacture = Column(String(250), nullable = False)
    cost_in_credits = Column(String(250), nullable = False)
    length = Column(String(250), nullable = False)
    max_atmosphering_speed = Column(String(250), nullable = False)
    crew = Column(String(250), nullable = False)
    passengers = Column(String(250), nullable = False)
    cargo_capacity = Column(String(250), nullable = False)
    consumables = Column(String(250), nullable = False)
    hyperdrive_rating = Column(String(250), nullable = False)
    MGLT = Column(String(250), nullable = False)
    starship_class = Column(String(250), nullable = False)
    pilots = Column(String(250), nullable = False)
    films = Column(String(250), nullable = False)

    favoritos = relationship("Favorito")

    def to_dict(self):
        return {}       
    

class Favorito(Base):
    __tablename__ = 'favorito'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user_id'), nullable=False)
    character_id = Column(Integer, ForeignKey('character_id'), nullable=True)
    planet_id = Column(Integer, ForeignKey('planet_id'), nullable=True)
    vehicle_id = Column(Integer, ForeignKey('vehicle_id'), nullable=True)

    user = relationship ("user")
    character = relationship ("character")
    planeta = relationship ("planeta")
    vehicle = relationship ("vehicle")



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
