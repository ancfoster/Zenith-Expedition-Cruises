/* jshint esversion: 11 */
// Init variables
const removeCont = document.getElementById('remove_cont');
const filterForm = document.getElementById('filter_form');
const tagSelect = document.getElementById('tag');
const urlParams = new URLSearchParams(window.location.search);
let tag;
tag = urlParams.get('tag');

// Submit filter form when value changed
tagSelect.addEventListener('change', () => {
    filterForm.submit();
})

window.onload = set;

// On load if a tag has been applied append a remove filter element
function set() {
    if (tag) {
        removeCont.innerHTML = `
        <a href="${url}">
        <span class="material-symbols-outlined">cancel</span>
        Remove '${tag}'
    </a>
        `
    }
}