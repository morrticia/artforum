from db import db


class ItemModel(db.Model):
    __tablename__ = 'collection'

    artist = db.Column(db.Integer, primary_key=True)
    artwork = db.Column(db.String)
    year = db.Column(db.String)

    def __init__(self, artist, artwork, year):
        self.artist = artist
        self.artwork = artwork
        self.year = year

    def json(self):
        return {"artist": self.artist, "artwork": self.artwork, "year": self.year}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(artist=name).first()

    @classmethod
    def get_items_from_collection(cls):
        return cls.query.all()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
