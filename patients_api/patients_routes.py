from flask import Blueprint, request, jsonify, redirect
from .patients_model import db, Patient

patients_bp = Blueprint('patients_bp', __name__)

@patients_bp.route('/', methods=['GET'])
def get_all_patients():
    """
    Fetch all patients, returning only their ID and patient_summary.
    """
    # SELECT id, patient_summary FROM patients;
    patients = Patient.query.with_entities(Patient.id, Patient.patient_summary).all()

    results = []
    for p in patients:
        results.append({"id": p.id, "patient_summary": p.patient_summary})

    return jsonify(results), 200


@patients_bp.route('/', methods=['POST'])
def create_patient():
    """
    Create a new patient record. Expects JSON data in the request body:
      {
        "patient_summary": "...",
        "real_time_alerts_insights": "...",
        "interventions_care_plan": "...",
        "timeline_gantt": "...",
        "raw_medical_record_data": "..."
      }
    """
    data = request.get_json(force=True)

    new_patient = Patient(
        patient_summary=data.get("patient_summary", ""),
        real_time_alerts_insights=data.get("real_time_alerts_insights", ""),
        interventions_care_plan=data.get("interventions_care_plan", ""),
        timeline_gantt=data.get("timeline_gantt", ""),
        raw_medical_record_data=data.get("raw_medical_record_data", "")
    )

    db.session.add(new_patient)
    db.session.commit()

    return jsonify({"message": "Patient created successfully", "id": new_patient.id}), 201


@patients_bp.route('/<int:patient_id>', methods=['PUT'])
def update_patient(patient_id):
    """
    Update an existing patient record by ID.
    """
    patient = Patient.query.get(patient_id)
    if not patient:
        return jsonify({"error": "Patient not found"}), 404

    data = request.get_json(force=True)
    patient.patient_summary = data.get("patient_summary", patient.patient_summary)
    patient.real_time_alerts_insights = data.get("real_time_alerts_insights", patient.real_time_alerts_insights)
    patient.interventions_care_plan = data.get("interventions_care_plan", patient.interventions_care_plan)
    patient.timeline_gantt = data.get("timeline_gantt", patient.timeline_gantt)
    patient.raw_medical_record_data = data.get("raw_medical_record_data", patient.raw_medical_record_data)

    db.session.commit()

    return jsonify({"message": f"Patient {patient_id} updated successfully"}), 200


@patients_bp.route('/<int:patient_id>/delete', methods=['POST', 'DELETE'])
def delete_patient(patient_id):
    """
    Delete an existing patient record by ID.
    """
    patient = Patient.query.get(patient_id)
    if not patient:
        return jsonify({"error": "Patient not found"}), 404

    db.session.delete(patient)
    db.session.commit()

    return flask.redirect('/')