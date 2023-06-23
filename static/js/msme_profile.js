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


// BUSINESS INFORMATION
function addSocialMedia() {
    var socialMedia = document.getElementById("social_media").value;
    var socialMediaLink = document.getElementById("social_media_link").value;
    var addedSocialMedia = document.getElementById("added_social_media");
  
    if (socialMedia !== "" && socialMediaLink !== "") {
        var newDiv = document.createElement("div");
        newDiv.className =
            "flex flex-col border border-t-0 border-myNavy divide-x-0 divide-y lg:divide-x lg:divide-y-0 divide-myNavy lg:flex-row";
  
        var newSocialMediaElement = document.createElement("div");
        newSocialMediaElement.className = "w-full px-2 py-2 lg:w-1/3";
        newSocialMediaElement.innerHTML =
            "<p class='ml-2 text-green-500'><span class='font-bold '>Added: </span>"
            + socialMedia +
            "</p>";
  
        var newSocialMediaLinkElement = document.createElement("div");
        newSocialMediaLinkElement.className = "flex w-full px-2 py-2 lg:w-2/3";
        newSocialMediaLinkElement.innerHTML =
            "<p class='ml-4 w-5/6 font-bold'>"
            + socialMediaLink +
            "</p>";
  
        var removeButton = document.createElement("button");
        removeButton.classList.add(
            "rounded", "bg-red-500", "hover:bg-red-600", "text-sm", "h-auto", "px-2", "py-2", "text-white", "font-bold", "w-1/6"
        );
        removeButton.innerHTML = "Remove";
        removeButton.addEventListener("click", function () {
            newDiv.remove();
        });
  
        newDiv.appendChild(newSocialMediaElement);
        newDiv.appendChild(newSocialMediaLinkElement);
        newSocialMediaLinkElement.appendChild(removeButton);
        addedSocialMedia.appendChild(newDiv);
  
        addedSocialMedia.style.display = "block";
  
        // Reset input fields
        document.getElementById("social_media").value = "";
        document.getElementById("social_media_link").value = "";
    }
}
  
