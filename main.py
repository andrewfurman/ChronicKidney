from flask import Flask
from dotenv import load_dotenv
import os

from patients_api.patients_routes import patients_bp
from patients_api.patients_model import db

load_dotenv()  # Load environment variables from .env

DATABASE_URL = os.getenv("DATABASE_URL")

app = Flask(__name__)

# Configure Flask app to use SQLAlchemy with your Postgres URL
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize the SQLAlchemy object with the Flask app
db.init_app(app)

# Create the patients table (and any other tables)
with app.app_context():
    db.create_all()

# Register the Blueprint for all patient-related routes under /patients
app.register_blueprint(patients_bp, url_prefix='/patients')

@app.route('/')
def index():
    return 'Hello from Flask + SQLAlchemy!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)