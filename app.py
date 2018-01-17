import connexion, jwt, os
from flask_injector import FlaskInjector
from connexion.resolver import RestyResolver
from flask_cors import CORS
from flask import request, jsonify


from container import configure

if __name__ == '__main__':
    app = connexion.App(__name__, specification_dir='swagger/')
    app.add_api('room_app.yaml', resolver=RestyResolver('api'))
    FlaskInjector(app=app.app, modules=[configure])
    # add CORS support
    CORS(app.app)

    #jwt validation
    @app.app.before_request
    def authorize_token():
        try:
            if request.method != 'OPTIONS':
                auth_header = request.headers.get("Authorization")
                token = auth_header.split(' ')[1]
                jwt.decode(token, os.environ['JWT_SECRET_KEY'])
        except Exception as e:
            return jsonify({"message": "{}".format(e)}), 401

    app.run(port=9090)
