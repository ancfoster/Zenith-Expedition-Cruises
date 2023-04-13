/* jshint esversion: 11 */
// Init variables
const durationMinus =  document.getElementById('duration-minus');
const durationPlus =  document.getElementById('duration-plus');
const durationField = document.getElementById('id_duration');
const durationSpan = document.getElementById('duration-span');
const cruiseEndSpan = document.getElementById('cruise-end');
const cruiseStartField = document.getElementById('id_start_date');
const cruiseEndField = document.getElementById('id_end_date');
let movements = document.getElementById('id_movements');
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
    for(let movement = 0; movement < movementsJSON.length; movement++) {
        createMovementContainer(movement);
    }
}

// Calculates the end date of the cruise using start date and duration
function calculateEndDate() {
    cruiseEndDate.setDate(cruiseStartDate.getDate() + (duration - 1));
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
        let contRemove = document.getElementById(duration)
        contRemove.remove();
        duration -= 1;
        durationField.value = duration;
        durationSpan.innerText = duration;
        calculateEndDate();
        movementsJSON.pop();
        jsonToString();
    }
})
durationPlus.addEventListener('click', () => {
    if (duration == 199) {
        alert('Cruise duration cannot exceed 199 days')
    } 
    else {
        duration++;
        durationField.value = duration;
        durationSpan.innerText = duration;
        calculateEndDate();
        createMovementJSON(1, movementsJSON.length);
        jsonToString();
        let newDayJsonId = duration;
        newDayJsonId--;
        createMovementContainer(newDayJsonId);
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
    <option value='D'>Destination</option>
    <option value='SD'>Sea Day</option>
    <option value='SC'>Scenic Cruising</option>
`;

let sdSelects = `
    <option value='D'>Destination</option>
    <option value='SD' selected>Sea Day</option>
    <option value='SC'>Scenic Cruising</option>
`;

let scSelects = `
    <option value='D'>Destination</option>
    <option value='SD'>Sea Day</option>
    <option value='SC' selected>Scenic Cruising</option>
`;

// Build movement containers 
function loadMovements() {
    if (movements.value) {
        alert(movements.value);
    }
    else {
        createMovementJSON(duration, 0);
        jsonToString();
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
        let count = i
        count++;
        let mcDate = document.getElementById(`${count}_Date`);
        mcDate.innerText = frontEndDate;
    }
    jsonToString();
}

// This function creates the HTML elements that represent each movement/day of the cruise and allows the user to modify them
function createMovementContainer(day) {  
    // Create the movement container  
    let i = day
    let newMcCont = document.createElement('div');
    newMcCont.setAttribute('class', 'mc_cont');
    newMcCont.setAttribute('id', movementsJSON[i].day);
    // Create top row of container
    let newTopRow = `
    <div class="mc_row_top">
    <span class="mc_day">Day <span class="day">${movementsJSON[i].day}</span></span><span class="mc_date" id="${movementsJSON[i].day}_Date">${movementsJSON[i].frontEndDate}</span>
    </div>
    `;
    // Determine movement type and create UI accordingly
    switch (movementsJSON[i].type) {
        case 'D':
            let destinationUiElements = `
            <label class="admin_form_label" for="${movementsJSON[i].day}_Type">Movement Type</label>
            <select class="admin_field" id="${movementsJSON[i].day}_Type">
            ${movementSelects}
            </select>
            <label class="admin_form_label" for="${movementsJSON[i].day}_Destination">Destination</label>
            <select class="admin_field" id="${movementsJSON[i].day}_Destination">
            ${destinationSelects}
            </select>
            `
            newMcCont.innerHTML = newTopRow + destinationUiElements;
            movementsCont.append(newMcCont);
        break;
        case 'SD':
            let seaDayUiElements = `
            <label class="admin_form_label" for="${movementsJSON[i].day}_Type">Movement Type</label>
            <select class="admin_field" id="${movementsJSON[i].day}_Type">
            ${sdSelects}
            </select>
            <label class="admin_form_label" for="${movementsJSON[i].day}_Description">Description (optional)</label>
            <input type="text" maxlength="120" class="admin_field" id="${movementsJSON[i].day}}_Description">
            `
            newMcCont.innerHTML = newTopRow + seaDayUiElements;
            movementsCont.append(newMcCont);
        break;
        case 'SC':
            let scenicCruisingUiElements = `
            <label class="admin_form_label" for="${movementsJSON[i].day}_Type">Movement Type</label>
            <select class="admin_field" id="${movementsJSON[i].day}_Type">
            ${scSelects}
            </select>
            <label class="admin_form_label" for="${movementsJSON[i].day}_Description">Description (required)</label>
            <input type="text" maxlength="120" class="admin_field" required id="${movementsJSON[i].day}}_Description">
            `
            newMcCont.innerHTML = newTopRow + scenicCruisingUiElements;
            movementsCont.append(newMcCont);
        break;
        default:
            console.log("Error when creating movement containers") 
    }    
}

movementsCont.addEventListener('change', function(e){
    const target = e.target;
    //Create array from target element ID
    const elementId = target.id.split('_');
    let movementId = parseInt(elementId[0]);
    let movementsJsonId = movementId;
    movementsJsonId -= 1;
    // Element type is obtained from elementId array
    const elementType = elementId[1];
    switch (elementType) {
        case 'Destination':
            // Update the movementJSON value when a destination is changed
            movementsJSON[movementsJsonId].destination = parseInt(target.value);
            jsonToString();
            break;
        case 'Type':
            if(target.value == 'SD') {
                if (movementsJSON[movementsJsonId].type == 'D') {
                    let elementsToRemove = `${movementId}_Destination`;
                    // Remove destination list for movement div
                    target.remove();
                    let selectRemove = document.getElementById(elementsToRemove);
                    selectRemove.remove();
                    // Remove label - get the label to remove using its for attribute
                    let labelRemove = document.querySelector(`label[for="${elementsToRemove}"]`);
                    labelRemove.remove();
                    // Add new description field and label
                    let parentCont = document.getElementById(movementId);
                    let newElements = `
                    <select class="admin_field" id="${movementId}_Type">
                    ${sdSelects}
                    </select>
                    <label class="admin_form_label" for="${movementId}_Description">Description (optional)</label>
                    <input type="text" maxlength="120" class="admin_field" id="${movementId}_Description">
                    `;
                    parentCont.innerHTML += newElements;
                    // Update movementsJSON
                    movementsJSON[movementsJsonId].destination = "";
                    movementsJSON[movementsJsonId].type = "SD";
                    movementsJSON[movementsJsonId].description = "";
                }
            } else if (target.value == 'D') {
                let elementsToRemove = `${movementId}_Description`;
                    // Remove destination list for movement div
                    target.remove();
                    let selectRemove = document.getElementById(elementsToRemove);
                    selectRemove.remove();
                    // Remove label - get the label to remove using its for attribute
                    let labelRemove = document.querySelector(`label[for="${elementsToRemove}"]`);
                    labelRemove.remove();
                    // Add new description field and label
                    let parentCont = document.getElementById(movementId);
                    let newElements = `
                    <select class="admin_field" id="${movementId}_Type">
                    ${movementSelects}
                    </select>
                    <label class="admin_form_label" for="${movementId}_Destination">Destination</label>
                    <select class="admin_field" id="${movementId}_Destination">
                    ${destinationSelects}
                    </select>
                    `;
                    parentCont.innerHTML += newElements;
                    // Update movementsJSON
                    let firstDestination = destinations[0];
                    movementsJSON[movementsJsonId].destination = parseInt(firstDestination.id);
                    movementsJSON[movementsJsonId].type = "D";
                    movementsJSON[movementsJsonId].description = "";
            } else if (target.value == 'SC') {
                if (movementsJSON[movementsJsonId].type == 'D') {
                    let elementsToRemove = `${movementId}_Destination`;
                    // Remove destination list for movement div
                    target.remove();
                    let selectRemove = document.getElementById(elementsToRemove);
                    selectRemove.remove();
                    // Remove label - get the label to remove using its for attribute
                    let labelRemove = document.querySelector(`label[for="${elementsToRemove}"]`);
                    labelRemove.remove();
                    // Add new description field and label
                    let parentCont = document.getElementById(movementId);
                    let newElements = `
                    <select class="admin_field" id="${movementId}_Type">
                    ${scSelects}
                    </select>
                    <label class="admin_form_label" for="${movementId}_Description">Description (required)</label>
                    <input type="text" maxlength="120" class="admin_field" required id="${movementId}_Description">
                    `;
                    parentCont.innerHTML += newElements;
                    // Update movementsJSON
                    movementsJSON[movementsJsonId].destination = "";
                    movementsJSON[movementsJsonId].type = "SC";
                    movementsJSON[movementsJsonId].description = "";
                }
            }
            jsonToString();
            break;
        }
    })

movementsCont.addEventListener('input', function(e) {
    const target = e.target;
    //Create array from target element ID
    const elementId = target.id.split('_');
    let movementId = parseInt(elementId[0]);
    let movementsJsonId = movementId;
    movementsJsonId -= 1;
    // Element type is obtained from elementId array
    let text = e.target.value;
    movementsJSON[movementsJsonId].description = text;
    jsonToString();
})


function jsonToString() {
    let movementsString = JSON.stringify(movementsJSON);
    movements.value = movementsString;
}