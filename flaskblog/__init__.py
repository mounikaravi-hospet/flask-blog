import bcrypt
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '24734d926c668821dfc04f9fcc234e5b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login' 
#'login' here is the function name of the route, same as we use for url_for()

login_manager.login_message_category = 'warning' 
#witthout this, the 'please login to access this page' message will appear without any styling


from flaskblog import routes
