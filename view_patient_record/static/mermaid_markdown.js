//  format both plain markdown text and mermaid markdown as needed for view patient record html page

// mermaid_markdown.js
// Format both plain markdown text and mermaid markdown as needed for view_patient_record.html page

document.addEventListener('DOMContentLoaded', () => {
  // If Mermaid is loaded via CDN or otherwise, initialize it.
  if (typeof mermaid !== 'undefined') {
    mermaid.initialize({ startOnLoad: true });
  }
});