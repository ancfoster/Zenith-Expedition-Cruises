/* jshint esversion: 11 */
// Init variables

//Form field vars
const numberField = document.getElementById('id_number_guests');
const selectedCategoryField = document.getElementById('id_selected_category');
const selectedSuiteField = document.getElementById('id_selected_suite');

const guestNumberSpan = document.getElementById('guest_span_count');
const plus = document.getElementById('plus');
const minus = document.getElementById('minus');
const categoryCont = document.getElementById('category_cont');

let numberGuests = 0;
let categorySelected = null;

// Suite selection vars
const suiteSelectionCont = document.getElementById('suite_selection_cont');
const deckplan = document.getElementById('deckplan');

// Price variables
const totalPriceVerandah = document.getElementById('total_price_verandah');
const totalPriceDeluxe = document.getElementById('total_price_deluxe');
const totalPriceSpa = document.getElementById('total_price_spa');
const totalPriceOwner = document.getElementById('total_price_owner');

// Guest form vars
let numberForms = 0;
const detailFormCont = document.getElementById('detail_form_cont');

window.onload = set;

function set() {
    let suitesParse = JSON.parse(suites);
    suites = suitesParse;
    let deckplansParse = JSON.parse(deckplans);
    deckplans = deckplansParse;
    numberGuests = 2;
    numberField.value = numberGuests;
    updateTotalPrice();
    createDetailForms();
}
// Updates total price based on number of passengers
function updateTotalPrice() {
    // 1 guest = 25% discount
    // 3 guests = 50% surcharge
    let multiplier = 0
    switch (numberGuests){
        case 1:
            multiplier = 0.75;
            break;
        case 2:
            multiplier = 1;
            break;
        case 3:
            multiplier = 1.5;
            break;
    }
    // Checks if price span exists, if so update the price based on multipler
    if (totalPriceVerandah) {
        totalPriceVerandah.innerText = (verandah_price * multiplier).toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
    }
    if (totalPriceDeluxe) {
        totalPriceDeluxe.innerText = (deluxe_price * multiplier).toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
    }
    if (totalPriceSpa) {
        totalPriceSpa.innerText = (spa_price * multiplier).toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
    }
    if (totalPriceOwner) {
        totalPriceOwner.innerText = (owner_price * multiplier).toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
    }
}

// Controls number of passengers increment buttons
plus.addEventListener('click', () => {
    if (numberGuests < 3) {
        createDetailForms();
        numberGuests++
        numberField.value = numberGuests
        guestNumberSpan.innerText = numberGuests;
        if (numberGuests === 3) {
            plus.style.cursor = "not-allowed";
        }
        if ( numberGuests > 1) {
            minus.style.cursor = "pointer";
        }
        updateTotalPrice();
    }
})
// Minus number of guests
minus.addEventListener('click', () => {
    if (numberGuests > 1) {
        deleteDetailForm();
        numberGuests--
        numberField.value = numberGuests
        guestNumberSpan.innerText = numberGuests;
        if (numberGuests === 1) {
            minus.style.cursor = "not-allowed";
        }
        if ( numberGuests < 3) {
            plus.style.cursor = "pointer";
        }
        updateTotalPrice();
    }
})

// Select and update category
categoryCont.addEventListener('click', (e) => {
  let categoryButtonSelected = e.target.closest('.suite_category');
  removeSelectedCategoryClass()
  let divId = categoryButtonSelected.id
  let toApply = document.getElementById(divId);
  toApply.classList.add('category_selected');
  switch (categoryButtonSelected.id){
    case 'verandah':
        categorySelected = 1;
        selectedCategoryField.value = 1;
        deckplan.src = updateDeckplan()
        break;
    case 'deluxe':
        categorySelected = 2;
        selectedCategoryField.value = 2;
        deckplan.src = updateDeckplan()
        break;
    case 'spa':
        categorySelected = 3;
        selectedCategoryField.value = 3;
        deckplan.src = updateDeckplan()
        break;
    case 'owner':
        categorySelected = 4;
        selectedCategoryField.value = 4;
        deckplan.src = updateDeckplan()
        break;
  }
  generateSuiteSelection();
})
// Removes the category selected class from any div that has it
function removeSelectedCategoryClass() {
    let toRemove = categoryCont.querySelectorAll('.category_selected');
    for (let i = 0; i < toRemove.length; i++) {
    toRemove[i].classList.remove('category_selected');
    }
}

// Suite selection functions
// Generate suite numbers based on category selection
function generateSuiteSelection() {
    suiteSelectionCont.innerHTML = ''
    // Loop through and get available suites that match selected category
    for(i = 0; i < suites.length; i++) {
        if (suites[i].category == categorySelected) {
            let suite = generateSuiteItem(suites[i].suite_number)
            suiteSelectionCont.innerHTML += suite;
        }
    }
}
// Generate the div for each suite button
function generateSuiteItem(x) {
    let suiteButton = `
    <div role="button" class="suite_item" id='${x}'>${x}</div>
    `;
    return suiteButton;
}
// Suite selection
suiteSelectionCont.addEventListener('click', (e) => {
    if (e.target.classList.contains('suite_item')) {
        removeSelectedSuiteClass()
        const suiteSelectedId = e.target.id;
        selectedSuiteField.value = parseInt(suiteSelectedId);
        let toApply = document.getElementById(suiteSelectedId);
        toApply.classList.add('suite_selected');
    }
  })
  // Removes the category selected class from any div that has it
function removeSelectedSuiteClass() {
    let toRemove = suiteSelectionCont.querySelectorAll('.suite_selected');
    for (let i = 0; i < toRemove.length; i++) {
    toRemove[i].classList.remove('suite_selected');
    }
}
  // Update deckplan image
function updateDeckplan() {
    for (let i = 0; i < deckplans.length; i++) {
        if (deckplans[i].category === categorySelected) {
            let url = deckplans[i].url;
            return url;
        }
    }
}

// Guest Details
function createDetailForms() {
    switch (numberForms) {
        case 0:
            detailFormCont.innerHTML += detailsTemplate(1);
            detailFormCont.innerHTML += detailsTemplate(2);
            numberForms = 2;
        break;
        case 1:
            detailFormCont.innerHTML += detailsTemplate(2);
            numberForms = 2;
        break;
        case 2:
            detailFormCont.innerHTML += detailsTemplate(3);
            numberForms = 3;
        break;
        default:
            break;
    }
}

function deleteDetailForm(){
    let formNumber = `guest${numberForms}`;
    let formToDelete = document.getElementById(formNumber);
    switch (numberForms) {
        case 2:
            formToDelete.remove()
            numberForms--;
            break;
        case 3:
            formToDelete.remove()
            numberForms--;
            break;
        default:
            break;
    }
}

function detailsTemplate(guest_number) {
    let formTemplate = `
    <form method="POST" action="" class="booking_form" id="guest${guest_number}">
        <h3 class="gf_center">Guest ${guest_number}</h3>
        <label for="first_name">First Name</label>
        <input type="text" id="first_name" maxlength="25" required>
        <label for="last_name">Last Name</label>
        <input type="text" required id="last_name" maxlength="25">
        <label for="dob">Date of Birth</label>
        <input type="date" required id="dob">
        <label for="passport_number" for="passport_number">Passport Number</label>
        <input type="number" required maxlength="20" id="passport_number">
        <label for="passport_expiry">Passport Expiry Date</label>
        <input type="date" min="{{ passport_min_expire }}" required id="passport_expiry">
        <label for="telephone">Telephone</label>
        <input type="tel" maxlength="16" required id="telephone">
        <label for="email">Email</label>
        <input type="email" id="email" maxlength="120" required>
    </form>
    `
    return formTemplate;
}