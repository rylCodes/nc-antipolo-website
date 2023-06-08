function toggleAltNavigation() {
    const altNavigation = document.getElementById("altNavigation");
    const menuButton = document.getElementById("menuButton");

    altNavigation.classList.toggle("hidden");
    altNavigation.classList.toggle("flex");

    if (altNavigation.classList.contains("flex")) {
        menuButton.classList.add("outline-none", "ring-2", "ring-skyBlue", "ring-offset-4");
    } else {
        menuButton.classList.remove("outline-none", "ring-2", "ring-skyBlue", "ring-offset-4");
    }
}

