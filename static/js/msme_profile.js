const level0Radio = document.getElementById("level_0");
const level1Radio = document.getElementById("level_1");
const level2Radio = document.getElementById("level_2");
const level3Radio = document.getElementById("level_3");
const level4Radio = document.getElementById("level_4");
const ceased = document.getElementById("ceased");
const subLevelOptions = document.getElementById("subLevelOptions");

function handleLevelChange() {
    if (level1Radio.checked) {
        subLevelOptions.style.display = "block";
    } else {
        subLevelOptions.style.display = "none";
    }
}

function handleOtherLevelsChange() {
    if (level0Radio.checked || level2Radio.checked || level3Radio.checked || level4Radio.checked || ceased.checked) {
        subLevelOptions.style.display = "none";
    } else {
        subLevelOptions.style.display = "block";
    }
}

level0Radio.addEventListener("change", handleOtherLevelsChange);
level1Radio.addEventListener("change", handleLevelChange);
level2Radio.addEventListener("change", handleOtherLevelsChange);
level3Radio.addEventListener("change", handleOtherLevelsChange);
level4Radio.addEventListener("change", handleOtherLevelsChange);
ceased.addEventListener("change", handleOtherLevelsChange);