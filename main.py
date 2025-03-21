# main.py

from flask import Flask
# Import the Blueprint from view_patient_routes
from view_patient_record.view_patient_routes import view_patient_record_bp

app = Flask(__name__)

# Register the blueprint with a URL prefix, e.g., "/patient"
app.register_blueprint(view_patient_record_bp, url_prefix='/patient')

@app.route('/')
def index():
    return 'Hello from Flask!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)