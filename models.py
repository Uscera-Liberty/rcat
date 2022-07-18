from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """User model"""
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username =db.Column(db.String(25) , unique = True ,nullable=True)
    password = db.Column(db.String(), nullable=False)

    db.create_all()