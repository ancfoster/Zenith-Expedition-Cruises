/* jshint esversion: 11 */
// Init variables
const DescriptionField = document.getElementById('id_description');
const DescriptionCount = document.getElementById('description_count');

DescriptionField.addEventListener('input', countLength);
function countLength(e) {
   DescriptionCount.textContent = `${e.target.value.length} / 700`;
}
