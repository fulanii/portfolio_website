function typewriterEffect(element, typeSpeed = 150, eraseSpeed = 100, delayBetweenTitles = 2000) {
    const jobTitles = ["Solopreneur", "Developer", "Freelancer", "Backend/Fullstack Engineer"];
    let index = 0;
    let isErasing = false;

    function type() {
        const currentText = jobTitles[index];

        if (!isErasing) {
            element.textContent = currentText.substring(0, element.textContent.length + 1);
            element.classList.add("typing");
            element.classList.remove("erasing");

            if (element.textContent.length === currentText.length) {
                isErasing = true;
                setTimeout(type, delayBetweenTitles);
            } else {
                setTimeout(type, typeSpeed);
            }
        } else {
            element.textContent = currentText.substring(0, element.textContent.length - 1);
            element.classList.add("erasing");
            element.classList.remove("typing");

            if (element.textContent.length === 0) {
                isErasing = false;
                index = (index + 1) % jobTitles.length;
                setTimeout(type, typeSpeed);
            } else {
                setTimeout(type, eraseSpeed);
            }
        }
    }

    setTimeout(type, 1000);
}

document.addEventListener("DOMContentLoaded", () => {
    const jobTitleSpan = document.querySelector(".hero-job__titles");
    typewriterEffect(jobTitleSpan);
});
