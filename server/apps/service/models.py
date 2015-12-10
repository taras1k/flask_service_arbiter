from extensions import db


class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    base_url = db.Column(db.String(255), nullable=False, unique=True)

