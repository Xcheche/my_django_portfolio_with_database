function submitForm(event) {
        event.preventDefault();

        // Assuming the form submission is successful
        // You can add your own form submission logic here if needed

        // Show the success message
        var successMessage = document.getElementById("success-message");
        successMessage.innerText = "Sent successfully. I normally respond within 48 hours. Also, feel free to WhatsApp me.";
        successMessage.style.display = "block";

        // Set a timeout to hide the success message after 5 seconds
        setTimeout(function () {
          successMessage.style.display = "none";
        }, 5000);

        // Reset the form fields (optional)
        event.target.reset();

        return false;
      }