// for navbar togglr on/off
export function toggleNavbar() {
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
// Ensure that the display style is reset based on the viewport width
window.addEventListener("resize", () => {
    const header = document.getElementById("header");
    const icon = document.querySelector(".header__nav__icon");

    // change 775 later
    if (window.innerWidth > 775) {
        header.removeAttribute("style");
    }
    // change 775 later
    if (window.innerWidth <= 775 && getComputedStyle(header).display === "none") {
        icon.classList.remove("bi-x");
        icon.classList.add("bi-list");
    }
});

// Active nav item on scroll
export function setActiveNavItem() {
    // Active nav item on scroll
    const navItems = document.querySelectorAll(".nav__item");
    const sections = document.querySelectorAll("section");

    let index = sections.length;

    while (--index && window.scrollY + 50 < sections[index].offsetTop) {}

    navItems.forEach((item) => item.classList.remove("active"));
    navItems[index].classList.add("active");
}

// Setup nav item click events
export function setupNavItemClicks() {
    const navItems = document.querySelectorAll(".nav__item");
    navItems.forEach((item) => {
        item.addEventListener("click", (e) => {
            navItems.forEach((navItem) => navItem.classList.remove("active"));
            item.classList.add("active");
        });
    });
}
