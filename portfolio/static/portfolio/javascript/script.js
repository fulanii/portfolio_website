import { toggleNavbar, setActiveNavItem, setupNavItemClicks } from "./components/navbar.js";

document.addEventListener("DOMContentLoaded", () => {
    // Navbar toggle
    document.querySelector(".icon-a").addEventListener("click", toggleNavbar);
    
    // Active nav item on scroll
    window.addEventListener("scroll", setActiveNavItem);
    setActiveNavItem();

    // Setup nav item click events
    setupNavItemClicks();

    // AOS animation
    AOS.init();
});
