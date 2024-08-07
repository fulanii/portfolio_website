// export function smoothScroll() {
//     const btn = document.querySelector(".projects-li");
//     const SectionToGoTO = document.querySelector("#projects");3

//     console.log(btn, SectionToGoTO)

//     btn.addEventListener("click", function (e) {
//         SectionToGoTO.scrollIntoView({ behavior: "smooth" });
//     });
// }

export function smoothScroll() {
    const allNavItems = document.querySelectorAll(".nav__item");

    const heroSection = document.querySelector("#hero");
    const aboutSection = document.querySelector("#about-me");
    const skillsSection = document.querySelector("#skills");
    const projectsSection = document.querySelector("#projects");

    allNavItems.forEach(function (tag, index) {
        tag.addEventListener("click", function (e) {
            if (index === 0) {
                // hero
                e.preventDefault(); // Prevent default anchor behavior

                heroSection.scrollIntoView({ behavior: "smooth" });
            } else if (index === 1) {
                // about
                e.preventDefault(); // Prevent default anchor behavior

                aboutSection.scrollIntoView({ behavior: "smooth" });
            } else if (index === 2) {
                // skills
                e.preventDefault(); // Prevent default anchor behavior

                skillsSection.scrollIntoView({ behavior: "smooth" });
            } else if (index === 3) {
                // projects
                e.preventDefault(); // Prevent default anchor behavior

                projectsSection.scrollIntoView({ behavior: "smooth" });
            }
        });
    });
}
