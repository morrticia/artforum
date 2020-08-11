from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from models.item import ItemModel


class Items(Resource):
    @jwt_required()
    def get(self):
        items = ItemModel.get_items_from_collection()
        list = []
        for item in items:
            list.append(item.json())
        return {'collection': list}


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('artist',
                        required=True,
                        location='json',
                        help="Enter the artist name")

    parser.add_argument('year',
                        required=True,
                        location='json',
                        help="Enter the year")

    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': f'We could not find {name}'}, 404

    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message': f'{name} already exists'}, 400

        try:
            data = Item.parser.parse_args()
        except Exception as e:
            return {'message': e}

        item = ItemModel(name, data['artist'], data['year'])
        try:
            item.save_to_db()
            return {'message': f'{name} has been added to collection'}, 400
        except Exception as e:
            return {'message': e}
        else:
            return item.json()

    def put(self, name):
        item = ItemModel.find_by_name(name)
        data = Item.parser.parse_args()

        if item:
            item.year = data['year']
            item.artist = data['artist']
        else:
            item = ItemModel(name, data['artist'], data['year'])

        item.save_to_db()
        return {'Item from collection: ': item.json()}

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return {'message': f'{name} is deleted'}
        else:
            return {'message': f'We could not find {name}'}

