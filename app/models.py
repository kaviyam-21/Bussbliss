from . import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    role = db.Column(db.String(10), nullable=False)  # crew or passenger
    region = db.Column(db.String(10))  # north or south (for crew)
    familiarity = db.Column(db.String(100))  # routes familiarity (for crew)
    availability = db.Column(db.Boolean, default=True)  # (for crew)
    shift = db.Column(db.String(50))  # (for crew)
    bus_route = db.Column(db.String(100))  # Assigned bus route (for crew)
    is_linked = db.Column(db.Boolean, default=False)  # Linked or unlinked duty
