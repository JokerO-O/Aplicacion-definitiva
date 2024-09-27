from flask import Flask
from app import db, bcrypt
from app.routes import app
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
bcrypt.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
