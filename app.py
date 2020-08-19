from flask import Flask, redirect
from flask_restful import Api
from flask_jwt import JWT

from security import authentication, identity

from resources.item import Items, Item
from resources.user import Account


from db import db

app = Flask(__name__)
app.secret_key = "TopSecret"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

jwt = JWT(app, authentication, identity)
api = Api(app)

@app.route('/')
def redirecturl():
    return redirect('https://documenter.getpostman.com/view/11843891/T1LPD7Ki?version=latest')


api.add_resource(Item, "/artwork/<string:name>")
api.add_resource(Items, "/artworks")
api.add_resource(Account, "/registration")

#
# @app.before_first_request
# def create_tables():
#     db.create_all()

if __name__ == "__main__":
    from db import db
    db.init_app(app)

    app.run(port=5000, debug=True)


