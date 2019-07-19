import os

from flask import Flask



def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI='mysql://cary:1qaz2wsxE@34.83.211.214/mysitedb'
    )
    
    from flask_app.models import db
    db.init_app(app)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World! This is from app factory'

    # register blueprints
    from .wechat import wx
    from .resume import resume
    app.register_blueprint(wx.bp)
    app.register_blueprint(resume.bp)

    return app