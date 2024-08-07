import { toggleNavbar, setActiveNavItem, setupNavItemClicks } from "./components/navbar.js";
import { typewriterEffect } from "./utils/typewriter.js";
import { smoothScroll } from "./utils/smoothScroll.js";


document.addEventListener("DOMContentLoaded", () => {
    // Navbar toggle
    document.querySelector(".icon-a").addEventListener("click", toggleNavbar);

    // Typewriter effect
    const jobTitleSpan = document.querySelector(".hero-job__titles");
    typewriterEffect(jobTitleSpan);

    // Active nav item on scroll
    window.addEventListener("scroll", setActiveNavItem);
    setActiveNavItem();

    // Setup nav item click events
    setupNavItemClicks();

    // smooth scrolling
    smoothScroll();

    // AOS animation
    AOS.init();
});
