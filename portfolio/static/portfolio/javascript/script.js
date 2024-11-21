// for navbar togglr on/off
function toggleNavbar() {
    const header = document.getElementById("header");
    const iconA = document.querySelector(".icon-a");
    const icon = document.querySelector(".header__nav__icon");
    const headerStyle = window.getComputedStyle(header);

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

    // AOS animation
    AOS.init();
});
