/* jshint esversion: 11 */
// Init variables
const durationMinus =  document.getElementById('duration-minus');
const durationPlus =  document.getElementById('duration-plus');
const durationField = document.getElementById('id_duration');
const durationSpan = document.getElementById('duration-span');
const cruiseEndSpan = document.getElementById('cruise-end');
const cruiseStartField = document.getElementById('id_start_date');
const cruiseEndField = document.getElementById('id_end_date');
const movements = document.getElementById('id_movements');
const movementsCont = document.getElementById('movements-container');
var destinationSelects = '';    
var cruiseStartDate = new Date();
let cruiseEndDate = new Date();
var duration;
let movementsJSON = [];
let destinations = {};

// Extract hidden field values
window.onload = loadValues;

function loadValues() {
    duration = parseInt(durationField.value);
    durationSpan.innerText = duration;
    cruiseStartDate = new Date(cruiseStartField.value);
    calculateEndDate();
    loadDestinations();
    loadMovements();
    createMovementContainers();
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
    updateDates();
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
        createMovementJSON(1, movementsJSON.length);
    }
})

// Get destinations and convert to JSON
function loadDestinations() {
    // rawDestinations is generated in the Django template
    let destinationsString = rawDestinations;
    destinations = JSON.parse(destinationsString);
    for(let i = 0; i < destinations.length; i++) {
        let destinationObject = destinations[i];
        let destId = destinationObject.id;
        let destName = destinationObject.name;
        let destCountry = destinationObject.country;
        if (i === 0) {
            let select = `<option selected value="${destId}">${destName}, ${destCountry}</option>`;
            destinationSelects += select;
        }
        else {
            let select = `<option value="${destId}">${destName}, ${destCountry}</option>`;
            destinationSelects += select;
        }
    }
}

let movementSelects = `
    <option value='D' selected >Destination</option>
    <option value='SD'>Sea Day</option>
    <option value='SC'>Scenic Cruising</option>
`;

// Build movement containers 
function loadMovements() {
    if (movements.value) {
        alert(movements.value);
    }
    else {
        createMovementJSON(duration, 0);
    }
}


function createMovementJSON(daysToCreate, dayFrom) {
    for(let i=0; i < daysToCreate; i++) {
        let day = dayFrom + (i + 1);
        let movementDate = new Date()
        movementDate.setDate(cruiseStartDate.getDate() + (day - 1));
        let movementDateDay = `${movementDate.getDate().toString().padStart(2, '0')}`;
        let movementDateMonth = `${(movementDate.getMonth() + 1).toString().padStart(2, '0')}`;
        let movementDateYear = `${movementDate.getFullYear().toString()}`;
        // Front End Date
        frontEndDate = `${movementDateDay}-${movementDateMonth}-${movementDateYear}`;
        // Back End Date
        backEndDate = `${movementDateYear}-${movementDateMonth}-${movementDateDay}`;
        let firstDestination = destinations[0];
        let newMovement = {
            'day': day,
            'frontEndDate': frontEndDate,
            'backEndDate': backEndDate,
            'type': 'D',
            'destination': firstDestination.id,
            'description': ''
        }
        movementsJSON.push(newMovement);
    }
    console.log(movementsJSON);
}

// Updates the movement JSON objects when the cruise date is changed.
function updateDates() {
    for (i = 0; i < movementsJSON.length; i++) {
        let movementDate = new Date()
        movementDate.setDate(cruiseStartDate.getDate() + i);
        let movementDateDay = `${movementDate.getDate().toString().padStart(2, '0')}`;
        let movementDateMonth = `${(movementDate.getMonth() + 1).toString().padStart(2, '0')}`;
        let movementDateYear = `${movementDate.getFullYear().toString()}`;
        // Front End Date
        frontEndDate = `${movementDateDay}-${movementDateMonth}-${movementDateYear}`;
        // Back End Date
        backEndDate = `${movementDateYear}-${movementDateMonth}-${movementDateDay}`;
        movementsJSON[i].frontEndDate = frontEndDate;
        movementsJSON[i].backEndDate = backEndDate;
    }
    console.log(movementsJSON);
}


function createMovementContainers() {
    console.log('Create movement cont')
    for(i = 0; i < movementsJSON.length; i++) {
        // Create new movement div container and give it the class mc_cont
        let newMcCont = document.createElement('div');
        newMcCont.setAttribute('class', 'mc_cont');
        newMcCont.setAttribute('id', movementsJSON[i].day);
        //Create top row of cruise movement container
        let newRowTop = document.createElement('div');
        // Add contents of top row (contains day and date values)
        newRowTop.setAttribute('class', 'mc_row_top');
        newRowTop.innerHTML = `
        <span class="mc_day">Day <span class="day">${movementsJSON[i].day}</span></span><span class="mc_date">${movementsJSON[i].frontEndDate}</span>
        `;
        // Create label for movement type select element
        let newTypeSelectLabel = document.createElement('label');
        newTypeSelectLabel.setAttribute('class', 'admin_form_label');
        newTypeSelectLabel.setAttribute('for', `${movementsJSON[i].day}_Type`);
        newTypeSelectLabel.innerText = 'Movement Type';
        // Create movement type select element
        let newTypeSelect = document.createElement('select');
        newTypeSelect.setAttribute('class', 'admin_field');
        newTypeSelect.setAttribute('id', `${movementsJSON[i].day}_Type`);
        newTypeSelect.innerHTML = movementSelects;
        newMcCont.append(newRowTop, newTypeSelectLabel, newTypeSelect);
        switch (movementsJSON[i].type) {
            case 'D':
                newTypeSelect.value = 'D'
                let newDestinationLabel = document.createElement('label');
                newDestinationLabel.setAttribute('class', 'admin_form_label');
                newDestinationLabel.setAttribute('for', `${movementsJSON[i].day}_Destination`);
                newDestinationLabel.innerText = 'Destination';
                let newDestinationSelect = document.createElement('select');
                newDestinationSelect.setAttribute('class', 'admin_field');
                newDestinationSelect.setAttribute('id', `${movementsJSON[i].day}_Destination`);
                newDestinationSelect.innerHTML = destinationSelects;
                newDestinationSelect.value = movementsJSON[i].destination;
                newMcCont.append(newDestinationLabel, newDestinationSelect);
                break;
            default:
                console.log("Error when creating movement containers")                
        }
        movementsCont.appendChild(newMcCont);        
    }
}

movementsCont.addEventListener('change', function(e){
    const target = e.target;
    const elementId = target.id.split('_');
    let movementId = parseInt(elementId[0]);
    movementId -= 1;
    const elementType = elementId[1];
    switch (elementType) {
        case 'Destination':
            movementsJSON[movementId].destination = parseInt(target.value);
            console.log(target.value)
            break;
        }
})
