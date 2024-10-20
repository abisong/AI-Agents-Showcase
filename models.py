from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Interaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    agent_type = db.Column(db.String(50), nullable=False)
    user_input = db.Column(db.Text, nullable=False)
    ai_response = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, server_default=db.func.now())

class PortfolioData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    asset_name = db.Column(db.String(100), nullable=False)
    asset_value = db.Column(db.Float, nullable=False)
    asset_type = db.Column(db.String(50), nullable=False)

class WorkflowTask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(200), nullable=False)
    assigned_to = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    due_date = db.Column(db.Date, nullable=False)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
