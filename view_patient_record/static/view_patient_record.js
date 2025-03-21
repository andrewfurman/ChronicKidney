// view_patient_record.js
// Main logic for editing the record, collapsing/expanding sections, etc.

document.addEventListener('DOMContentLoaded', () => {
  const editBtn = document.getElementById('edit-btn');
  const toggleButtons = document.querySelectorAll('.toggle-section');
  const sectionContents = document.querySelectorAll('.section-content');

  let isEditing = false;

  // Toggle collapse/expand for each section
  toggleButtons.forEach((btn) => {
    btn.addEventListener('click', () => {
      const parentSection = btn.closest('.collapsible');
      const contentDiv = parentSection.querySelector('.section-content');
      if (contentDiv.style.display === 'none') {
        contentDiv.style.display = 'block';
      } else {
        contentDiv.style.display = 'none';
      }
    });
  });

  // Toggle edit mode for all content sections
  editBtn.addEventListener('click', () => {
    isEditing = !isEditing;
    sectionContents.forEach((sec) => {
      sec.contentEditable = isEditing;
    });
    editBtn.textContent = isEditing ? 'Save' : 'Edit';
  });
});