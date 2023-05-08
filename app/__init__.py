from flask import Flask

from config import Config

from .api.routes import api

from .auth.routes import auth

from .models import db, User
from flask_migrate import Migrate
from flask_cors import CORS
from flask_login import LoginManager
# from flask_bootstrap import Bootstrap


app = Flask(__name__)
# Bootstrap(app)

# from flask.cors import CORS (under.models)

login = LoginManager()

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)


app.config.from_object(Config)

CORS(app, resources={r"/*": {"origins": "*"}})

db.init_app(app)
migrate = Migrate(app, db)

login.init_app(app)

login.login_view = 'auth.loginPage'


app.register_blueprint(auth)
app.register_blueprint(api)


from . import routes

