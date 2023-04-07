const durationMinus =  document.getElementById('duration-minus');
const durationPlus =  document.getElementById('duration-plus');
const durationField = document.getElementById('id_duration');
const durationSpan = document.getElementById('duration-span');
const cruiseEndSpan = document.getElementById('cruise-end');
const cruiseStartField = document.getElementById('id_start_date');

let cruiseStartDate
let cruiseEndDate
let duration

window.onload = loadValues();

function loadValues() {
    duration = parseInt(durationField.value);
    durationSpan.innerText = duration;
    cruiseStartDate = Date(cruiseStartField.value);
    cruiseEndDate.setDate(cruiseEndDate + duration);
    cruiseEndSpan.innerText = cruiseEndDate
}

cruiseStartField.addEventListener('change', () => {
    cruiseStartDate = Date(cruiseStartField.value);
})

durationMinus.addEventListener('click', () => {
    if (duration == 2) {
        alert('Cruise duration cannot be less than two days')
    } 
    else {
        duration -= 1;
        durationField.value = duration;
        durationSpan.innerText = duration;
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
    }
})