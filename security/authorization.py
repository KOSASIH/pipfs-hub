from flask_jwt import JWTManager

jwt_manager = JWTManager()


def setup_authorization(app):
    # Set up access control using Flask-JWT or Django Rest Framework

    jwt_manager.init_app(app)
