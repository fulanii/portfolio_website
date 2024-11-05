const forms = document.querySelectorAll(".cta-form");

document.getElementById("cta-options").addEventListener("change", function (even) {
    const selectedOption = this.value;
    const selectedForm = document.getElementById(`form-${selectedOption}`);

    forms.forEach((form) => form.classList.add("hidden")); // Hide all forms initially
    forms.forEach((form) => (form.style.display = "none"));

    if (selectedOption) {
        selectedForm.classList.remove("hidden"); // Show selected form
        selectedForm.style.display = "flex";
    }
});
