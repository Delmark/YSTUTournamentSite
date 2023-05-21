// Team formatation script
let team_struct = document.querySelector("#team_struct");
let match_sched = document.querySelector("#match_sched");
let team_static = document.querySelector("#team_static");

team_struct.onclick = function() {
    flagDiv.classList.add("openedStruct");
    flagDiv.classList.remove("openedSched");
    flagDiv.classList.remove("openedStatist");
}

match_sched.onclick = function() {
    flagDiv.classList.remove("openedStruct");
    flagDiv.classList.add("openedSched");
    flagDiv.classList.remove("openedStatist");
}

team_static.onclick = function() {
    flagDiv.classList.remove("openedStruct");
    flagDiv.classList.remove("openedSched");
    flagDiv.classList.add("openedStatist");
}