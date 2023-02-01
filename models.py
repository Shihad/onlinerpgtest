from flask_sqlalchemy import SQLAlchemy
import random

db = SQLAlchemy()

class Personage(db.Model):
    __tablename__="personages"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    hp = db.Column(db.Integer)
    max_hp = db.Column(db.Integer)
    attack = db.Column(db.Integer)
    defence = db.Column(db.Integer)

    def __init__(self, name):
        self.name=name
        self.max_hp = random.randint(100,110)
        self.hp=self.max_hp
        self.attack=10
        self.defence=10

    def __repr__(self):
        return f"{self.name} has {self.hp} of {self.max_hp}"