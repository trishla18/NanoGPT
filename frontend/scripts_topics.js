document.addEventListener("DOMContentLoaded", () => {
  const joinButtons = document.querySelectorAll(".join-btn");

  joinButtons.forEach((button) => {
    button.addEventListener("click", () => {
      alert("You have joined the subject!");
    });
  });
});
