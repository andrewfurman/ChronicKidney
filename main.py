# main.py

from flask import Flask, render_template
from dotenv import load_dotenv
import os

from patients_api.patients_model import db, Patient
from patients_api.patients_routes import patients_bp

# Import your "view_patient_record" blueprint
from view_patient_record.view_patient_routes import view_patient_record_bp

load_dotenv()  # Load environment variables from .env
DATABASE_URL = os.getenv("DATABASE_URL")

app = Flask(__name__, template_folder='view_patient_record/templates')

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
with app.app_context():
    db.create_all()

# Register your "patients" blueprint
# e.g. all endpoints under /patients, such as GET /patients/
app.register_blueprint(patients_bp, url_prefix='/patients')

# Register the "view_patient_record" blueprint under /view_patient_record
app.register_blueprint(view_patient_record_bp, url_prefix='/view_patient_record')

@app.route('/')
def index():
    patients = Patient.query.all()
    # Renders the "all_patient_records.html" template
    return render_template('all_patient_records.html', patients=patients)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)