# Main application file
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from app.routes import api, web
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app)

app.register_blueprint(api)
app.register_blueprint(web)

if __name__ == '__main__':
    app.run(debug=True)
