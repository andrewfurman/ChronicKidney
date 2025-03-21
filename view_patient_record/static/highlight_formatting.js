// Use Highlight.js to format code blocks in the view_patient_record.html page

// highlight_formatting.js
// Use Highlight.js to format code blocks in the view_patient_record.html page

document.addEventListener('DOMContentLoaded', () => {
  // If highlight.js is loaded via CDN or another script tag, proceed
  if (typeof hljs !== 'undefined') {
    // Find all <pre> or <code> blocks and highlight them
    document.querySelectorAll('pre, code').forEach((block) => {
      hljs.highlightElement(block);
    });
  }
});