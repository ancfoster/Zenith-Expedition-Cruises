/* jshint esversion: 11 */
// Init variables
const durationMinus =  document.getElementById('duration-minus');
const durationPlus =  document.getElementById('duration-plus');
const durationField = document.getElementById('id_duration');
const durationSpan = document.getElementById('duration-span');
const cruiseEndSpan = document.getElementById('cruise-end');
const cruiseStartField = document.getElementById('id_start_date');
const cruiseEndField = document.getElementById('id_end_date');
let cruiseStartDate = new Date();
let cruiseEndDate = new Date();
let duration;

// Extract hidden field values
window.onload = loadValues;

function loadValues() {
    duration = parseInt(durationField.value);
    durationSpan.innerText = duration;
    cruiseStartDate = new Date(cruiseStartField.value);
    calculateEndDate();
}

// Calculates the end date of the cruise using start date and duration
function calculateEndDate() {
    cruiseEndDate.setDate(cruiseStartDate.getDate() + duration);
    let cruiseEndDateDay = `${cruiseEndDate.getDate().toString().padStart(2, '0')}`;
    let cruiseEndDateMonth = `${(cruiseEndDate.getMonth() + 1).toString().padStart(2, '0')}`;
    let cruiseEndDateYear = `${cruiseEndDate.getFullYear().toString()}`;
    // Displayed to user in dd-mm-yyyy format
    cruiseEndSpan.innerText = `${cruiseEndDateDay}-${cruiseEndDateMonth}-${cruiseEndDateYear}`;
    // This value is returned to backend in yyyy-mm-dd format
    cruiseEndField.value = `${cruiseEndDateYear}-${cruiseEndDateMonth}-${cruiseEndDateDay}`;
}


// When the user changes the start date in the picker update hidden field value, recalculate end date
cruiseStartField.addEventListener('change', () => {
    cruiseStartDate = new Date(cruiseStartField.value);
    calculateEndDate();
})

// These two functions respond to the + - buttons being pressed then recalculate the cruise end date
durationMinus.addEventListener('click', () => {
    if (duration == 2) {
        alert('Cruise duration cannot be less than two days')
    } 
    else {
        duration -= 1;
        durationField.value = duration;
        durationSpan.innerText = duration;
        calculateEndDate();
    }
})
durationPlus.addEventListener('click', () => {
    if (duration == 199) {
        alert('Cruise duration cannot exceed 199 days')
    } 
    else {
        duration += 1;
        durationField.value = duration;
        durationSpan.innerText = duration;
        calculateEndDate();
    }
})