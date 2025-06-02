from flask import Flask, render_template, session, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
from routes import routes

load_dotenv()

app = Flask(__name__, static_url_path="")

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

app.config['SQLALCHEMY_DATABASE_URI'] = (f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

print("DB URI:", app.config['SQLALCHEMY_DATABASE_URI'])
print("Loaded password from .env:", os.getenv("DB_PASSWORD"))

#Initialize db FIRST
db = SQLAlchemy(app)

#THEN import models that use `db`
from models import *

#Then initialize migration
migrate = Migrate(app, db)

app.register_blueprint(routes)

@app.route("/")
def home():
    email = session.get("email")
    if not email or email == "null":
        return render_template("auth.html")
    return redirect("/game")

@app.route("/game")
def game():
    return render_template("game.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
