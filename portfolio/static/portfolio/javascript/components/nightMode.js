// Night Mode Toggle Component
// Defaults to night mode (dark mode)

const NIGHT_MODE_KEY = "nightMode";
const NIGHT_MODE_CLASS = "night-mode";

// Apply night mode immediately to prevent flash of light mode
(function () {
    const savedMode = localStorage.getItem(NIGHT_MODE_KEY);
    const isNightMode = savedMode === null ? true : savedMode === "true";

    if (isNightMode) {
        document.documentElement.classList.add(NIGHT_MODE_CLASS);
    }
})();

// Initialize night mode on page load
function initNightMode() {
    // Check localStorage, default to true (night mode) if not set
    const savedMode = localStorage.getItem(NIGHT_MODE_KEY);
    const isNightMode = savedMode === null ? true : savedMode === "true";

    // Apply night mode (already applied, but ensure it's correct)
    if (isNightMode) {
        document.documentElement.classList.add(NIGHT_MODE_CLASS);
    } else {
        document.documentElement.classList.remove(NIGHT_MODE_CLASS);
    }

    // Update toggle icon
    updateToggleIcon(isNightMode);
}

// Toggle night mode
function toggleNightMode() {
    const isCurrentlyNightMode = document.documentElement.classList.contains(NIGHT_MODE_CLASS);
    const newNightModeState = !isCurrentlyNightMode;

    // Toggle the class
    if (newNightModeState) {
        document.documentElement.classList.add(NIGHT_MODE_CLASS);
    } else {
        document.documentElement.classList.remove(NIGHT_MODE_CLASS);
    }

    // Save to localStorage
    localStorage.setItem(NIGHT_MODE_KEY, newNightModeState.toString());

    // Update toggle icon
    updateToggleIcon(newNightModeState);
}

// Update the toggle icon based on current mode
function updateToggleIcon(isNightMode) {
    const toggleIcon = document.querySelector(".night-toggle i");
    if (toggleIcon) {
        if (isNightMode) {
            // Show sun icon when in night mode (to switch to light mode)
            toggleIcon.classList.remove("bi-moon");
            toggleIcon.classList.add("bi-sun");
        } else {
            // Show moon icon when in light mode (to switch to night mode)
            toggleIcon.classList.remove("bi-sun");
            toggleIcon.classList.add("bi-moon");
        }
    }
}

// Setup event listener for night mode toggle
document.addEventListener("DOMContentLoaded", () => {
    // Initialize night mode (defaults to dark)
    initNightMode();

    // Add click event to night mode toggle button
    const nightToggle = document.querySelector(".night-toggle");
    if (nightToggle) {
        nightToggle.addEventListener("click", toggleNightMode);
    }
});
