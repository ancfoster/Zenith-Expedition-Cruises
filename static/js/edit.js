/* jshint esversion: 11 */
// Init variables
const nameCount = document.getElementById('name_count');
const descriptionCount = document.getElementById('description_count');
const nameField = document.getElementById('id_name');
const descriptionField = document.getElementById('id_description');

// Displays a count of the title & description input fields
nameField.addEventListener('input', countName);
function countName(e) {
   nameCount.textContent = `${e.target.value.length} / 120`;
}
descriptionField.addEventListener('input', countDescription);
function countDescription(e) {
   descriptionCount.textContent = `${e.target.value.length} / 360`;
}