// Active nav item on scroll
function setActiveNavItem() {
    // Active nav item on scroll
    const navItems = document.querySelectorAll(".nav__item");
    const sections = document.querySelectorAll("section");

    let index = sections.length;

    while (--index && window.scrollY + 50 < sections[index].offsetTop) {}

    navItems.forEach((item) => item.classList.remove("active"));
    navItems[index].classList.add("active");
}

// Setup nav item click events
function setupNavItemClicks() {
    const navItems = document.querySelectorAll(".nav__item");
    navItems.forEach((item) => {
        item.addEventListener("click", (e) => {
            navItems.forEach((navItem) => navItem.classList.remove("active"));
            item.classList.add("active");
        });
    });
}

document.addEventListener("DOMContentLoaded", () => {


    // Active nav item on scroll
    window.addEventListener("scroll", setActiveNavItem);
    setActiveNavItem();

    // Setup nav item click events
    setupNavItemClicks();
});
