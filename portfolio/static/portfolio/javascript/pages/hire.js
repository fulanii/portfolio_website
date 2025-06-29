"use strict";

const webDevBtn = document.querySelector(".web-dev-btn");
const wscrapingBtn = document.querySelector(".scraping-btn");
const apiBtn = document.querySelector(".api-btn");
const closeBtns = document.querySelectorAll(".close");
const button = document.querySelector(".hire-cta-button");
const noCodeBtn = document.querySelector(".no-code-btn");
const bookCallBtn = document.querySelectorAll(".modal-cta");
const modal = document.querySelectorAll(".modal");
const calLogo = document.querySelector(".text-subtle");

webDevBtn.addEventListener("click", (event) => {
    openModal("modal-web-dev");
});
wscrapingBtn.addEventListener("click", (event) => {
    openModal("modal-web-scraping");
});
apiBtn.addEventListener("click", (event) => {
    openModal("modal-rest-api");
});
noCodeBtn.addEventListener("click", (event) => {
    openModal("modal-no-code");
});
bookCallBtn.forEach((btn) => {
    btn.addEventListener("click", (event) => {
        window.scrollTo({
            top: document.querySelector("#my-cal-inline").offsetTop,
            behavior: "smooth"
        });

        modal.forEach((modal) => {
            // If the modal is open, close it
            if (modal.style.display === "flex") {
                modal.style.display = "none";
                document.body.style.overflow = "auto"; // Enable scrolling
            }
        });

        event.preventDefault(); // Prevent default action if it's a link
        event.stopPropagation(); // Stop the event from bubbling up
        return false; // Prevent any further action
    });
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

document.addEventListener("DOMContentLoaded", function () {
    calLogo.style.display = "none"; // Hide the Calendly logo
});
