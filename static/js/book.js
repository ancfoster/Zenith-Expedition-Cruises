/* jshint esversion: 11 */
// Init variables

//Form field vars
const numberField = document.getElementById('id_number_guests');
const selectedCategoryField = document.getElementById('id_selected_category');
const selectedSuiteField = document.getElementById('id_selected_suite');
const bookingForm = document.getElementById('booking_form');
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

//Container vars
const numberCategoryJourneyCont = document.getElementById('number_and_category_cont');
const suiteJourneyCont = document.getElementById('suite');
const guestDetailsCont = document.getElementById('guest_details');
const suiteCategoryButton = document.getElementById('suite_category_button');
const guestDetailsButton = document.getElementById('guest_details_button');
//Progress indiccator vars
const progressSuite = document.getElementById('progress_suite');
const progressGuests = document.getElementById('progress_guests');

// Guest form vars
let numberForms = 0;
const detailFormCont = document.getElementById('detail_form_cont');
let guestInfoList = []
const guestInformationField = document.getElementById('id_guest_information');

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
    guestDetailsCont.style.display = 'none';
    suiteJourneyCont.style.display = 'none';
    suiteCategoryButton.style.display = 'none';
    guestDetailsButton.style.display = 'none';
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
  // Update form progress
  suiteCategoryButton.style.display = 'flex';
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
    guestDetailsButton.style.display = 'flex';
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
            createGuestJson();
            detailFormCont.innerHTML += detailsTemplate(2);
            createGuestJson();
            numberForms = 2;
        break;
        case 1:
            detailFormCont.innerHTML += detailsTemplate(2);
            createGuestJson();
            numberForms = 2;
        break;
        case 2:
            detailFormCont.innerHTML += detailsTemplate(3);
            createGuestJson();
            numberForms = 3;
        break;
        default:
            break;
    }
}
// Delete guest information forms when number of guests is reduced
function deleteDetailForm(){
    let formNumber = `guest${numberForms}`;
    let formToDelete = document.getElementById(formNumber);
    switch (numberForms) {
        case 2:
            formToDelete.remove()
            guestInfoList.pop();
            numberForms--;
            break;
        case 3:
            formToDelete.remove()
            guestInfoList.pop();
            numberForms--;
            break;
        default:
            break;
    }
}
// Generates a new guest information form when guest number is increased
function detailsTemplate(guest_number) {
    let formTemplate = `
    <form method="POST" action="" class="booking_form" id="guest${guest_number}">
        <h3 class="gf_center">Guest ${guest_number}</h3>
        <label for="${guest_number}first_name">First Name</label>
        <input type="text" id="${guest_number}first_name" maxlength="25" required>
        <label for="${guest_number}last_name">Last Name</label>
        <input type="text" required id="${guest_number}last_name" maxlength="25">
        <label for="${guest_number}dob">Date of Birth</label>
        <input type="date" required id="${guest_number}dob">
        <label for="passport_number" for="${guest_number}passport_number">Passport Number</label>
        <input type="number" required maxlength="20" id="${guest_number}passport_number">
        <label for="${guest_number}passport_expiry">Passport Expiry Date</label>
        <input type="date" min="${passportExp}" required id="${guest_number}passport_expiry">
        <label for="${guest_number}telephone">Telephone</label>
        <input type="tel" maxlength="16" required id="${guest_number}telephone">
        <label for="${guest_number}email">Email</label>
        <input type="email" id="${guest_number}email" maxlength="120" required>
    </form>
    `;
    return formTemplate;
}
// Creates a new JSON object which is appended to the guestInfolist
function createGuestJson() {
    let obj = {"first_name": "","last_name": "","dob": "", "passport_number": "","passport_expiry": "","telephone": "","email": ""};
    guestInfoList.push(obj);
};
// Looks for when the guest forms are edited, updates the guestInfoList with new information
detailFormCont.addEventListener('input', e => {
    let target = e.target;
    if (target.tagName === 'INPUT' || target.tagName === 'SELECT' || target.tagName) {
        let targetId = String(target.id)
        guest = targetId.charAt(0)
        guest_number = parseInt(guest);
        let field = targetId.substring(1)
        switch (field) {
            case 'first_name':
                guestInfoList[(guest_number - 1)].first_name = target.value;
                    break;
                case 'last_name':
                guestInfoList[(guest_number - 1)].last_name = target.value;
                    break;
                case 'dob':
                guestInfoList[(guest_number - 1)].dob = target.value;
                    break;
                case 'passport_number':
                guestInfoList[(guest_number - 1)].passport_number = target.value;
                    break;
                case 'passport_expiry':
                guestInfoList[(guest_number - 1)].passport_expiry = target.value;
                    break;
                case 'telephone':
                guestInfoList[(guest_number - 1)].telephone = target.value;
                    break;
                case 'email':
                guestInfoList[(guest_number - 1)].email = target.value;
                    break;            
            default:
                break;
        }
    }
})

bookingForm.addEventListener('submit', e => {
    e.preventDefault();
    let guestInformationStr = JSON.stringify(guestInfoList);
    guestInformationField.value = guestInformationStr;
    bookingForm.submit();
})

suiteCategoryButton.addEventListener('click', () => {
    numberCategoryJourneyCont.style.display='none';
    suiteJourneyCont.style.display='flex';
})

guestDetailsButton.addEventListener('click', () => {
    suiteJourneyCont.style.display='none';
    guestDetailsCont.style.display='flex';
    progressSuite.classList.remove('booking_status_current');
    progressGuests.classList.add('booking_status_current');
})