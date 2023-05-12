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
