const mobileNavigation = document.getElementById("mobileNavigation");
const menuButton = document.getElementById("menuButton");

menuButton.addEventListener('click', () => {
    menuButton.classList.toggle('active');
    mobileNavigation.classList.toggle("hidden");
    mobileNavigation.classList.toggle("flex");
})
