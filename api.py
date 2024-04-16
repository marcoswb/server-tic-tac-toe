from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from src.controllers_api.login import Login
from src.controllers_api.register import Register

app = Flask(__name__)
CORS(app)

api = Api(app)

api.add_resource(Login, '/login')
api.add_resource(Register, '/register')

if __name__ == '__main__':
    app.run()