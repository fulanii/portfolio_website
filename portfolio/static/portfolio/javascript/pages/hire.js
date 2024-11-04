"use strict";

const webDevBtn = document.querySelector(".web-dev-btn");
const wscrapingBtn = document.querySelector(".scraping-btn");
const apiBtn = document.querySelector(".api-btn");
const body = document.body;
const closeBtns = document.querySelectorAll(".close");

webDevBtn.addEventListener("click", (event) => {
    openModal("modal-web-dev");
});
wscrapingBtn.addEventListener("click", (event) => {
    openModal("modal-web-scraping");
});
apiBtn.addEventListener("click", (event) => {
    openModal("modal-rest-api");
});

function openModal(modalId) {
    document.getElementById(modalId).style.display = "flex";
    document.body.style.overflow = "hidden";
}
function closeModal(modalId) {
    document.getElementById(modalId).style.display = "none";
    document.body.style.overflow = "auto"; // Enable scrolling
}

closeBtns.forEach((button) => {
    button.addEventListener("click", function () {
        // Find the parent modal (closest element with the class 'modal')
        const modal = button.closest(".modal");

        if (modal) {
            modal.style.display = "none";
            document.body.style.overflow = "auto"; // Enable scrolling
        }
    });
});
// Close the modal if the user clicks outside the content area
window.onclick = function (event) {
    document.querySelectorAll(".modal").forEach((modal) => {
        if (event.target == modal) {
            document.body.style.overflow = "auto"; // Enable scrolling
            modal.style.display = "none";
        }
    });
};
