const formsDivs = document.querySelectorAll(".cta-form");
const questionForm = document.querySelector(".q-form");
const allForms = document.querySelectorAll(".form");

document.getElementById("cta-options").addEventListener("change", function (even) {
    const selectedOption = this.value;
    const selectedForm = document.getElementById(`form-${selectedOption}`);

    formsDivs.forEach((form) => form.classList.add("hidden")); // Hide all forms initially
    formsDivs.forEach((form) => (form.style.display = "none"));

    if (selectedOption) {
        selectedForm.classList.remove("hidden"); // Show selected form
        selectedForm.style.display = "flex";
    }
});

allForms.forEach(function (indivudualForm) {
    indivudualForm.addEventListener("submit", function (event) {
        event.preventDefault();
        fetch(this.action, {
            method: this.method,
            body: new FormData(this)
        })
            .then((response) => {
                if (response.ok) {
                    return response.json();
                }
                else{
                    console.log("ErrorRes:", response);
                }
            })
            .then((data) => {
                if (data["success"] === true) {
                    this.reset();
                    alert("Form submitted successfully!"); // Optional success message
                } else {
                    alert("Form submitmission failed try again later");
                }
            })
            .catch((error) => {
                console.log("Error:", error);
                alert("There was an error submitting the form."); // Optional error message
            });
    });
});
