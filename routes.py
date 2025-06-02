from flask import Blueprint, jsonify, request, session
from app import db
from models import *
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date
import re

# 200: OK (success)
# 201: Created
# 400: Bad request (e.g. missing fields)
# 401: Unauthorized (not logged in)
# 403: Forbidden (logged in but not allowed)
# 404: Not Found (user/word/game not found)
# 409: Conflict (duplicate signup)

routes = Blueprint("routes", __name__)

def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

@routes.route("/api/signup", methods = ["POST"])
def signup():
    data = request.get_json()

    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if not username or not email or not password:
        return jsonify({"error": "all fields are required"}), 400
    
    if not is_valid_email(email):
        return jsonify({"error": "invalid email"}), 400
    
    existing_user = User.query.filter_by(username = username).first()
    if existing_user:
        return jsonify({"error": "username already exists"}), 409
    
    hashed_password = generate_password_hash(password)

    new_user = User(username = username, email = email, password = hashed_password)

    db.session.add(new_user)
    db.session.commit()

    session.permanent = True
    session["email"] = email

    return jsonify({"message": "Signup was successful"}), 201
    
@routes.route("/api/login", methods = ["POST"])
def login():
    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "all fields are required"}), 400
    
    user = User.query.filter_by(email = email).first()
    if not user:
        return jsonify({"error": "incorrect email"}), 404
    
    if not check_password_hash(user.password, password):
        return jsonify({"error": "Incorrect password"}), 401
    
    session.permanent = True
    session["email"] = email

    return jsonify({"message": "Login was successful"}), 200

    
