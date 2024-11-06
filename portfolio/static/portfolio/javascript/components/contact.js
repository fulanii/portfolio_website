const forms = document.querySelectorAll(".cta-form");
const questionForm = document.querySelector(".q-form");

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

questionForm.addEventListener("submit", function (event) {
    // setTimeout(() => {
    //     questionForm.reset();
    // }, 1000);

    event.preventDefault();

    // Replace this fetch with actual form submission handling
    fetch(this.action, {
        method: this.method,
        headers: { "X-CSRFToken": "{{ csrf_token }}" },
        body: new FormData(this)
    })
        .then((response) => {
            console.log(response);
            if (response.ok) {
                return response.json();
            }
        })
        .then((data) => {
            if (data["success"] === true) {
                this.reset();
                alert("Form submitted successfully!"); // Optional success message
            }
        })
        .catch((error) => {
            console.error("Error:", error);
            alert("There was an error submitting the form."); // Optional error message
        });
});
