# view_patient_routes.py

from flask import Blueprint, render_template

# Create a Blueprint for the "view_patient_record" module
# The 'template_folder' and 'static_folder' here assume you have this directory layout:
#  view_patient_record/
#    templates/
#      view_patient_record.html
#    static/
#      (your .js files)
view_patient_record_bp = Blueprint(
    'view_patient_record',
    __name__,
    template_folder='templates',
    static_folder='static'
)

# Route for displaying the patient record page
@view_patient_record_bp.route('/view')
def show_patient_record():
    # This should load 'view_patient_record.html' from the blueprint’s template folder
    return render_template('view_patient_record.html')