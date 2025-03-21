# Need to have a single database table to store:

# primary key 
# 1.	Patient Summary (Text)
# 2.	Real-Time Alerts & Insights (text)
# 3.	Interventions / Care Plan (text)
# 4.	Timeline / Gantt (text)
# 5.	Raw Medical Record Data (text)

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Patient(db.Model):
    __tablename__ = 'patients'

    id = db.Column(db.Integer, primary_key=True)
    patient_summary = db.Column(db.Text, nullable=True)
    real_time_alerts_insights = db.Column(db.Text, nullable=True)
    interventions_care_plan = db.Column(db.Text, nullable=True)
    timeline_gantt = db.Column(db.Text, nullable=True)
    raw_medical_record_data = db.Column(db.Text, nullable=True)