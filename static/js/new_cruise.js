/* jshint esversion: 11 */
// Init variables
const durationMinus =  document.getElementById('duration-minus');
const durationPlus =  document.getElementById('duration-plus');
const durationField = document.getElementById('id_duration');
const durationSpan = document.getElementById('duration-span');
const cruiseEndSpan = document.getElementById('cruise-end');
const cruiseStartField = document.getElementById('id_start_date');
const cruiseEndField = document.getElementById('id_end_date');
const movements = document.getElementById('movements');
const movementsCont = document.getElementById('movements-container');
var cruiseStartDate = new Date();
let cruiseEndDate = new Date();
var duration;
let movementsJSON;

// Extract hidden field values
window.onload = loadValues;

function loadValues() {
    duration = parseInt(durationField.value);
    durationSpan.innerText = duration;
    cruiseStartDate = new Date(cruiseStartField.value);
    calculateEndDate();
    loadDestinations();
    //loadMovements();
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
cruiseStartField.onchange = () => {
    cruiseStartDate = new Date(cruiseStartField.value);
    cruiseEndDate = new Date(cruiseStartDate.getTime());
    calculateEndDate();
    alert(cruiseEndDate)
}

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

// Get destinations and convert to JSON
function loadDestinations() {
    // rawDestinations is generated in the Django template
    let destinationsString = rawDestinations;
    let destinations = JSON.parse(destinationsString);
    var destinationSelects = '';    
    for(let i = 0; i < destinations.length; i++) {
        let destinationObject = destinations[i];
        let destId = destinationObject.id;
        let destName = destinationObject.name;
        let destCountry = destinationObject.country;
        let select = `<option>value="${destId}">${destName}, ${destCountry}</option>`;
        destinationSelects += select;
    }
}

let movementSelects = `
<select>
    <option value='D'>Destination</option>
    <option value='SD'>Sea Day</option>
    <option value='SC'>Scenic Cruising</option>
</select>

`;

// function loadMovements()
//     if (movements.value) {
//         // do nothing
//     }
//     else {

//     }