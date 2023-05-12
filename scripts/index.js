// Registration and log in script
let reglog_close_btn = document.querySelector("#reglog_close-button");
let regist_btn_header = document.querySelector("#registration-button_header");
let logIn_btn_header = document.querySelector("#logIn-button_header");
let regist_btn_footer = document.querySelector("#registration-button_footer");
let logIn_btn_footer = document.querySelector("#logIn-button_footer");
let flagDiv = document.querySelector("#flag");
let header = document.querySelector("#header");

reglog_close_btn.onclick = function() {
    flagDiv.classList.remove("openedRegLog");
}

regist_btn_header.onclick = function() {
    flagDiv.classList.add("openedRegLog");
    header.scrollIntoView({
        block: 'nearest',
        behavior: 'smooth',
    });
}

logIn_btn_header.onclick = function() {
    flagDiv.classList.add("openedRegLog");
    header.scrollIntoView({
        block: 'nearest',
        behavior: 'smooth',
    });
}

regist_btn_footer.onclick = function() {
    flagDiv.classList.add("openedRegLog");
    header.scrollIntoView({
        block: 'nearest',
        behavior: 'smooth',
    });
}

logIn_btn_footer.onclick = function() {
    flagDiv.classList.add("openedRegLog");
    header.scrollIntoView({
        block: 'nearest',
        behavior: 'smooth',
    });
}


// Carousel script
var slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
    showSlides(slideIndex += n);
}

function currentSlide(n) {
    showSlides(slideIndex = n);
}

function showSlides(n) {
    var i;
    var slides = document.getElementsByClassName("slide");
    var indicators = document.getElementsByClassName("sld-ind");

    if (n > slides.length) {slideIndex = 1}
    if (n < 1) {slideIndex = slides.length}
    for (i  = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    for (i = 0; i < indicators.length; i++) {
        indicators[i].className = indicators[i].className.replace(" active", "");
    }

    slides[slideIndex - 1].style.display = "block";
    indicators[slideIndex - 1].className += " active";
}

setInterval (
    () => plusSlides(1),
    6000
);