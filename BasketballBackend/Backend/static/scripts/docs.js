

// Docs formatation script
let doc_link = document.getElementsByClassName("document-link");

var i;
for (i = 0; i < doc_link.length; i++) {
    if ((i + 1) % 2 != 0) {
        doc_link[i].style = "margin-left: 50%";
    }
}