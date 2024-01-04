// DTI,SEC,CDA Office Address List
const dtiButton = document.getElementById("dtiButton");
const dtiList = document.getElementById("dtiList");

const secButton = document.getElementById("secButton");
const secList = document.getElementById("secList");

const cdaButton = document.getElementById("cdaButton");
const cdaList = document.getElementById("cdaList");

dtiButton.addEventListener("click", () => {
  dtiList.classList.toggle("hidden");
})

secButton.addEventListener("click", ()=> {
  secList.classList.toggle("hidden")
})

cdaButton.addEventListener("click", function() {
  cdaList.classList.toggle("hidden");
})


// BIR Office Address List
const birButton = document.getElementById("birButton");
const birList = document.getElementById("birList");

birButton.addEventListener("click", function() {
  birList.classList.toggle("hidden");
})

// BPLO-Antipolo Address List
const lguButton = document.getElementById("lguButton");
const lguList = document.getElementById("lguList");

lguButton.addEventListener("click", function() {
  lguList.classList.toggle("hidden");
})


// Social Agencies Office Address List
const sssButton = document.getElementById("sssButton");
const sssList = document.getElementById("sssList");

const philHealthButton = document.getElementById("philHealthButton");
const philHealthList = document.getElementById("philHealthList");

const pagIbigButton = document.getElementById("pagIbigButton");
const pagIbigList = document.getElementById("pagIbigList");

sssButton.addEventListener("click", ()=> {
  sssList.classList.toggle("hidden");
})

philHealthButton.addEventListener("click", ()=> {
  philHealthList.classList.toggle("hidden")
})

pagIbigButton.addEventListener("click", ()=> {
  pagIbigList.classList.toggle("hidden");
})


// Learn Business Type
const learnBusinessTypeLabel = document.getElementById("learnBusinessTypeLabel");
const learnBusinessTypeList = document.getElementById("learnBusinessTypeList");
const learnBusinessTypeDetails = document.getElementById("learnBusinessTypeDetails");

learnBusinessTypeLabel.addEventListener("click", ()=> {
  learnBusinessTypeList.classList.toggle("hidden");
})