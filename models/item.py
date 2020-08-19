from db import db


class ItemModel(db.Model):
    __tablename__ = 'collection'

    artist = db.Column(db.String)
    artwork = db.Column(db.String, primary_key=True)
    year = db.Column(db.String)
    category = db.Column(db.String)
    review = db.Column(db.String)

    def __init__(self, artist, artwork, year, category, review):
        self.artist = artist
        self.artwork = artwork
        self.year = year
        self.category = category
        self.review = review

    def json(self):
        return {"artist": self.artist, "artwork": self.artwork, "year": self.year, "category": self.category, "review": self.review}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(artwork=name).first()

    @classmethod
    def get_items_from_collection(cls):
        return cls.query.all()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
