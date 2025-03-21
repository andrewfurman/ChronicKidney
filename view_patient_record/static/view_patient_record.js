// view_patient_record/static/view_patient_record.js

document.addEventListener("DOMContentLoaded", function () {
  const addButton = document.getElementById("addPatientButton");
  if (addButton) {
    addButton.addEventListener("click", submitPatient);
  }
});

function submitPatient() {
  // Grab the form data
  const form = document.getElementById("patientForm");
  const formData = new FormData(form);

  // Build a JSON payload
  const payload = {
    patient_summary: formData.get("patient_summary"),
    real_time_alerts_insights: formData.get("real_time_alerts_insights"),
    interventions_care_plan: formData.get("interventions_care_plan"),
    timeline_gantt: formData.get("timeline_gantt"),
    raw_medical_record_data: formData.get("raw_medical_record_data"),
  };

  // Send a JSON POST request
  fetch("/patients/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error(`Request failed with status ${response.status}`);
      }
      return response.json();
    })
    .then((data) => {
      console.log("Success:", data);
      // Optionally refresh or redirect
      window.location.reload();
    })
    .catch((error) => {
      console.error("Error:", error);
      alert("Error creating patient. See console for details.");
    });
}