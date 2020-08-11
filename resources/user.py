import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel


class Account(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        required=True,
                        location='json',
                        help="Enter username")

    parser.add_argument('password',
                        required=True,
                        location='json',
                        help="Enter password")
    TABLE = "users"

    def post(self):
        try:
            userdata = Account.parser.parse_args()
        except Exception as e:
            print(e)
            return {'message': e}
        if UserModel.find_by_username(userdata['username']):
            return {'message': f'{userdata["username"]} already exists'}, 400
        else:
            try:
                user = UserModel(UserModel.idgenerator(), userdata['username'], userdata['password'])
                user.add_account()
                return {"message": "Signed up"}
            except:
                return {"message": "Sign up not possible"}

    def delete(self):
        try:
            userdata = Account.parser.parse_args()
        except Exception as e:
            return e
        if UserModel.find_by_username(userdata['username']):
            try:
                UserModel.find_by_username(userdata['username']).delete_account()
                return {"message": "Account deleted"}
            except:
                return {"message": "Could not delete this account"}
        else:
            return {"message": "Could not find this account"}