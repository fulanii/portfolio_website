

// for navbar togglr on/off
function toggleNavbar() {
    const header = document.getElementById("header");
    const iconA = document.querySelector(".icon-a");
    const icon = document.querySelector(".header__nav__icon");
    const headerStyle = window.getComputedStyle(header);

    const nightToggle = document.querySelector(".night-toggle i");

    // is header showing: hide
    if (headerStyle.display === "flex") {
        header.style.display = "none";
        icon.classList.remove("bi-x");
        icon.classList.add("bi-list");
    } else {
        // if header hidden: show
        header.style.display = "inline-flex";
        icon.classList.remove("bi-list");
        icon.classList.add("bi-x");
    }

    if (nightToggle.classList.contains("bi-moon")){
        header.style.backgroundColor = "white"
    } else {
        header.style.backgroundColor = "#1f2933"
    }
}

// night mode on/off
function nightMode(){
    const body = document.querySelector("body");
    const nightToggle = document.querySelector(".night-toggle i");
    const allNavLinks = document.querySelectorAll(".nav__link");
    const allSocialLinks = document.querySelectorAll(".social__a");
    const allSkillsLi =  document.querySelectorAll(".skill-card li");
    const skillCard = document.querySelectorAll(".skill-card");
    const headerCover = document.getElementById("header")

    if (nightToggle.classList.contains("bi-moon")) {
        nightToggle.classList.remove("bi-moon");
        nightToggle.classList.add("bi-sun");
    
        body.style.backgroundColor = "#1f2933";
        body.style.color = "white";
        allNavLinks.forEach((link) => {
            link.style.color = "white";
        });
        allSocialLinks.forEach((link) => {
            link.style.color = "white";
        });
        allSkillsLi.forEach((li) => {
            li.style.color = "white";
        });
        skillCard.forEach((card) => {
            card.style.backgroundColor = "#1f2933";
        });
        headerCover.style.backgroundColor = "#1f2933"
    }
    else {
        nightToggle.classList.remove("bi-sun");
        nightToggle.classList.add("bi-moon");
    
        body.style.backgroundColor = "white";
        body.style.color = "black";
        allNavLinks.forEach((link) => {
            link.style.color = "black";
        });
        allSocialLinks.forEach((link) => {
            link.style.color = "black";
        });
        allSkillsLi.forEach((li) => {
            li.style.color = "black";
        });
        skillCard.forEach((card) => {
            card.style.backgroundColor = "white";
        });
        headerCover.style.backgroundColor = "white"

    }
}

document.addEventListener("DOMContentLoaded", () => {
    // Ensure that the display style is reset based on the viewport width
    window.addEventListener("resize", () => {
        const header = document.getElementById("header");
        const icon = document.querySelector(".header__nav__icon");

        if (window.innerWidth > 775) {
            header.removeAttribute("style");
        }
        if (window.innerWidth <= 775 && getComputedStyle(header).display === "none") {
            icon.classList.remove("bi-x");
            icon.classList.add("bi-list");
        }
    });

    document.addEventListener("DOMContentLoaded", () => {
        const arrowIcon = document.querySelector(".scroll-btn i");
        arrowIcon.style.animation = "jump 1s infinite ease-in-out";
    });

    // Navbar toggle
    document.querySelector(".icon-a").addEventListener("click", toggleNavbar);

    // night toggle
    document.querySelector(".night-toggle").addEventListener("click", nightMode);

    // AOS animation
    AOS.init();
});
