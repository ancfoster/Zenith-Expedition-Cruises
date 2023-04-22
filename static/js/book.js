/* jshint esversion: 11 */
// Init variables
const numberField = document.getElementById('id_number_guests');
const guestNumberSpan = document.getElementById('guest_span_count');
const plus = document.getElementById('plus');
const minus = document.getElementById('minus');
let count = 0;

window.onload = setCount;

function setCount() {
    count = 2;
    numberField.value = count
}

// Controls number of passengers increment buttons
plus.addEventListener('click', () => {
    if (count < 3) {
        count++
        numberField.value = count
        guestNumberSpan.innerText = count;
        if (count === 3) {
            plus.style.cursor = "not-allowed";
        }
        if ( count > 1) {
            minus.style.cursor = "pointer";
        }
    }
})
// Minus number of guests
minus.addEventListener('click', () => {
    if (count > 1) {
        count--
        numberField.value = count
        guestNumberSpan.innerText = count;
        if (count === 1) {
            minus.style.cursor = "not-allowed";
        }
        if ( count < 3) {
            plus.style.cursor = "pointer";
        }
    }
})