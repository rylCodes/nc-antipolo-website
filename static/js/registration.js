// Register your business now!
const businessNameSelect = document.getElementById("businessNameSelect");
const birSelect = document.getElementById("birSelect");
const lguSelect = document.getElementById("lguSelect");
const socialAgencySelect = document.getElementById("socialAgencySelect");
const businessNameRegister = document.getElementById("businessNameRegister");
const birRegister = document.getElementById("birRegister");
const lguRegister = document.getElementById("lguRegister");
const socialAgencyRegister = document.getElementById("socialAgencyRegister");

businessNameSelect.addEventListener("click", function() {
  if (businessNameRegister.style.display === 'none') {
    businessNameRegister.style.display = 'block';
    birRegister.style.display = 'none';
    lguRegister.style.display = 'none';
    socialAgencyRegister.style.display = 'none';
  } else {
    businessNameRegister.style.display = 'none';
  }
})

birSelect.addEventListener("click", function() {
  if (birRegister.style.display === 'none') {
    birRegister.style.display = 'block';
    businessNameRegister.style.display = 'none';
    lguRegister.style.display = 'none';
    socialAgencyRegister.style.display = 'none';
  } else {
    birRegister.style.display = 'none';
  }
})

lguSelect.addEventListener("click", function() {
  if (lguRegister.style.display === 'none') {
    lguRegister.style.display = 'block';
    birRegister.style.display = 'none';
    businessNameRegister.style.display = 'none';
    socialAgencyRegister.style.display = 'none';
  } else {
    lguRegister.style.display = 'none';
  }
})

socialAgencySelect.addEventListener("click", function() {
  if (socialAgencyRegister.style.display === 'none') {
    socialAgencyRegister.style.display = 'block';
    birRegister.style.display = 'none';
    lguRegister.style.display = 'none';
    businessNameRegister.style.display = 'none';
  } else {
    socialAgencyRegister.style.display = 'none';
  }
})


// DTI,SEC,CDA Office Address List
const dtiButton = document.getElementById("dtiButton");
const dtiList = document.getElementById("dtiList");

const secButton = document.getElementById("secButton");
const secList = document.getElementById("secList");

const cdaButton = document.getElementById("cdaButton");
const cdaList = document.getElementById("cdaList");

document.addEventListener("click", function(event) {
  if (event.target !== dtiButton && event.target !== secButton && event.target !== cdaButton){
    dtiList.style.display = "none";
    secList.style.display = "none";
    cdaList.style.display = "none";
  }
})

dtiButton.addEventListener("click", function() {
  if (dtiList.style.display === "none") {
    dtiList.style.display = "block";
  } else {
    dtiList.style.display = "none";
  }
})

secButton.addEventListener("click", function() {
  if(secList.style.display === "none") {
    secList.style.display = "block";
  } else {
    secList.style.display = "none";
  }
})

cdaButton.addEventListener("click", function() {
  if(cdaList.style.display === "none") {
    cdaList.style.display = "block";
  } else {
    cdaList.style.display = "none";
  }
})


// BIR Office Address List
const birButton = document.getElementById("birButton");
const birList = document.getElementById("birList");

document.addEventListener("click", function(event) {
  if (event.target !== birButton){
    birList.style.display = "none";
  }
})

birButton.addEventListener("click", function() {
  if (birList.style.display === "none") {
    birList.style.display = "block";
  } else {
    birList.style.display = "none";
  }
})

// BPLO-Antipolo Address List
const lguButton = document.getElementById("lguButton");
const lguList = document.getElementById("lguList");

document.addEventListener("click", function(event) {
  if (event.target !== lguButton){
    lguList.style.display = "none";
  }
})

lguButton.addEventListener("click", function() {
  if (lguList.style.display === "none") {
    lguList.style.display = "block";
  } else {
    lguList.style.display = "none";
  }
})


// Social Agencies Office Address List
const sssButton = document.getElementById("sssButton");
const sssList = document.getElementById("sssList");

const philHealthButton = document.getElementById("philHealthButton");
const philHealthList = document.getElementById("philHealthList");

const pagIbigButton = document.getElementById("pagIbigButton");
const pagIbigList = document.getElementById("pagIbigList");

document.addEventListener("click", function(event) {
  if (event.target !== sssButton && event.target !== philHealthButton && event.target !== pagIbigButton){
    sssList.style.display = "none";
    philHealthList.style.display = "none";
    pagIbigList.style.display = "none";
  }
})

sssButton.addEventListener("click", function() {
  if (sssList.style.display === "none") {
    sssList.style.display = "block";
  } else {
    sssList.style.display = "none";
  }
})

philHealthButton.addEventListener("click", function() {
  if (philHealthList.style.display === "none") {
    philHealthList.style.display = "block";
  } else {
    philHealthList.style.display = "none";
  }
})

pagIbigButton.addEventListener("click", function() {
  if (pagIbigList.style.display === "none") {
    pagIbigList.style.display = "block";
  } else {
    pagIbigList.style.display = "none";
  }
})


// Learn Business Type
const learnBusinessTypeLabel = document.getElementById("learnBusinessTypeLabel");
const learnBusinessTypeList = document.getElementById("learnBusinessTypeList");
const learnBusinessTypeDetails = document.getElementById("learnBusinessTypeDetails");
const imgBNR = document.getElementById("imgBNR");

document.addEventListener("click", function(event) {
  if (event.target !== learnBusinessTypeLabel && event.target !== learnBusinessTypeDetails && event.target !== learnBusinessTypeList) {
    learnBusinessTypeList.style.display = "none";
    imgBNR.style.display = "flex";
  }
})

learnBusinessTypeLabel.addEventListener("click", function() {
  if (learnBusinessTypeList.style.display === "none") {
    learnBusinessTypeList.style.display = "block";
    imgBNR.style.display = "none";
  } else {
    learnBusinessTypeList.style.display = "none";
    imgBNR.style.display = "flex";
  }
})