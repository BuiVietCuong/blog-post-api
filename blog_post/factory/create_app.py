from flask import Flask
from marshmallow import ValidationError

from blog_post.app.auth.routes import auth_blue_print
from blog_post.app.blog_post.routes import blog_post_blue_print
from blog_post.factory.constants import JWT_SECRET_KEY
from blog_post.factory.error_handler import handle_validation_error, handle_exception

from flask_jwt_extended import JWTManager

from db_utils import db, migrate


def create_app() -> Flask:
    app = Flask(
        __name__,
    )

    # Setup the Flask-JWT-Extended extension
    app.config["JWT_SECRET_KEY"] = JWT_SECRET_KEY
    jwt = JWTManager(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    '''
        Register error handler
    '''
    app.register_error_handler(ValidationError, handle_validation_error)
    app.register_error_handler(Exception, handle_exception)

    '''
        Register blue print
    '''
    app.register_blueprint(blog_post_blue_print, url_prefix='/api/blog-post/')
    app.register_blueprint(auth_blue_print, url_prefix='/api/auth/')
    return app
