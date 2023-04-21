/* jshint esversion: 11 */
// Init variables
const numberField = document.getElementById('id_passengers_for_booking');
const passengerNumberSpan = document.getElementById('passenger_span_count');
const plus = document.getElementById('plus');
const minus = document.getElementById('minus');
let count = 0;

window.onload = setCount;

function setCount() {
    count = 2;
    numberField.value = count
}

plus.addEventListener('click', () => {
    if (count < 3) {
        count++
        numberField.value = count
        passengerNumberSpan.innerText = count;
        if (count === 3) {
            plus.style.cursor = "not-allowed";
        }
        if ( count > 1) {
            minus.style.cursor = "pointer";
        }
    }
})

minus.addEventListener('click', () => {
    if (count > 1) {
        count--
        numberField.value = count
        passengerNumberSpan.innerText = count;
        if (count === 1) {
            minus.style.cursor = "not-allowed";
        }
        if ( count < 3) {
            plus.style.cursor = "pointer";
        }
    }
})