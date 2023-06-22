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
  