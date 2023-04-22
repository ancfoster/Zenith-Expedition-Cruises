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

// Price variables
const totalPriceVerandah = document.getElementById('total_price_verandah');
const totalPriceDeluxe = document.getElementById('total_price_deluxe');
const totalPriceSpa = document.getElementById('total_price_spa');
const totalPriceOwner = document.getElementById('total_price_owner');

window.onload = set;

function set() {
    let suitesParse = JSON.parse(suites);
    suites = suitesParse;
    numberGuests = 2;
    numberField.value = numberGuests
    updateTotalPrice()
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
        break;
    case 'deluxe':
        categorySelected = 2;
        selectedCategoryField.value = 2;
        break;
    case 'spa':
        categorySelected = 3;
        selectedCategoryField.value = 3;
        break;
    case 'owner':
        categorySelected = 4;
        selectedCategoryField.value = 4;
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
      let toRemove = categoryCont.querySelectorAll('.suite_selected');
      for (let i = 0; i < toRemove.length; i++) {
      toRemove[i].classList.remove('suite_selected');
      }
  }