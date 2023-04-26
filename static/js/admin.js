/* jshint esversion: 11 */
const burgerCont = document.getElementById('burgerCont');
const burgerIcon = document.getElementById('burgerIcon');
const adminNav = document.getElementById('adminNav');
let menuStatus = 0;

burgerCont.addEventListener("click", () => {
    if (menuStatus === 0) {
        burgerIcon.innerHTML = 'close';
        menuStatus += 1;
        adminNav.style.transform = 'translateX(0px)';
    } else {
        burgerIcon.innerHTML = 'menu';
        menuStatus -= 1;
        adminNav.style.transform = 'translateX(-100%)';
    }
});