from flask import Flask, render_template
from flask_ckeditor import CKEditor
from flask_sqlalchemy import SQLAlchemy
from flask_loginmanager import LoginManager
from flask_migrate import Migrate

# Create a Flask Instance
app = Flask(__name__)
# Add CKEditor
# ckeditor = CKEditor(app)
# Add Database
# Old SQLite DB
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://fvmdxyjigwbmiu:d31d36c7613e08f7ad37a6e40007189d7f2f44fbc99234b339994780a122d870@ec2-3-214-190-189.compute-1.amazonaws.com:5432/d17b5scj97ckqe'
# New MySQL DB
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/db_name'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password123@localhost/our_users'
# Secret Key!
# app.config['SECRET_KEY'] = "my super secret key that no one is supposed to know"
# Initialize The Database

# UPLOAD_FOLDER = 'static/images/'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

# Flask_Login Stuff
# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'login'


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/user/<name>")
def user(name):
    return render_template("user.html", name=name)


# create custom error pages
# invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


# invalid URL
@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500


if __name__ == "__main__":
    app.run(debug=True)
