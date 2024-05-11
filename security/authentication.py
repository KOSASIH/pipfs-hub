from flask_login import LoginManager

login_manager = LoginManager()

def setup_authentication(app):
    # Set up user authentication using Flask-Login

    login_manager.init_app(app)
    login_manager.login_view = 'login'
