# view_patient_record/view_patient_routes.py

from flask import Blueprint, render_template

view_patient_record_bp = Blueprint(
    'view_patient_record',
    __name__,
    template_folder='templates',
    static_folder='static'
)

# Example route if you want /view_patient_record/view
@view_patient_record_bp.route('/view')
def show_patient_record():
    return render_template('view_patient_record.html')