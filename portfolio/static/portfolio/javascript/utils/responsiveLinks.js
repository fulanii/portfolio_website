function adjustLinkWidth() {
    const linksDiv = document.querySelector(".links-div");
    const width = window.innerWidth;

    // Ensure minWidth is set initially
    if (!linksDiv.style.minWidth) {
        linksDiv.style.minWidth = getComputedStyle(linksDiv).minWidth;
    }

    // Ensure minWidth is numeric
    const currentWidth = parseInt(getComputedStyle(linksDiv).minWidth, 10);

    // Adjust width only when it decreases by 10px increments
    if (width <= 570 && width % 10 === 0) {
        const newWidth = currentWidth - 10;
        linksDiv.style.minWidth = `${newWidth}px`;
    }
}

// window.addEventListener("resize", adjustLinkWidth);
