from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Token(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(100), unique=True, nullable=False)
    expireon = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"Token('{self.token}', '{self.expireon}')"

# if __name__ == '__main__':
#     from flask import Flask
#     app = Flask(__name__)
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://cary:1qaz2wsxE@34.83.211.214/mysitedb'
#     db.init_app(app)
#     with app.app_context():
#         db.create_all()