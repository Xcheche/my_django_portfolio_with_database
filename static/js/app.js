function submitForm(event) {
        event.preventDefault();

        // Assuming the form submission is successful
        // You can add your own form submission logic here if needed

        // Show the success message
        var successMessage = document.getElementById("success-message");
successMessage.innerText = "Message Sent! 🎉\n" +
  "Thank you for reaching out. I typically respond within 48 hours.\n" +
  "In the meantime, if you need an immediate response or have any urgent questions, feel free to drop me a message on WhatsApp.";

        successMessage.style.display = "block";

        // Set a timeout to hide the success message after 5 seconds
        setTimeout(function () {
          successMessage.style.display = "none";
        }, 5000);

        // Reset the form fields (optional)
        event.target.reset();

        return false;
      }


    //Splashscreen
      const splash = document.querySelector(".splash");
      document.addEventListener("DOMContentLoaded", (event) => {
        setTimeout(() => {
          splash.classList.add("display-none");
        }, 3000);
      });


//Theme forwebsite
// var icon = document.getElementById("icon");

// icon.onclick = function () {
//   document.body.classList.toggle("dark-theme");
//   if (document.body.classList.contains("dark-theme")) {
//     icon.src = "{% static 'images/sun.jpg' %}";
//   } else {
//     icon.src = "{% static 'images/moon.jpg' %}";
//   } 
// }
var icon = document.getElementById("icon");

icon.onclick = function () {
    document.body.classList.toggle("dark-theme");
    if (document.body.classList.contains("dark-theme")) {
        icon.src = "{% static 'images/sun.png' %}";
    } else {
        icon.src = "{% static 'images/moon.png' %}";
    }
}
