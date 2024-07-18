document.addEventListener("DOMContentLoaded", () => {
  const sendBtn = document.getElementById("send-btn");
  const chatPrompt = document.getElementById("chat-prompt");
  const chatHistory = document.getElementById("chat-history");

  sendBtn.addEventListener("click", () => {
    const userInput = chatPrompt.value;
    if (userInput.trim() !== "") {
      appendMessage(userInput, "user-message");
      chatPrompt.value = "";
      botResponse(userInput);
    }
  });

  chatPrompt.addEventListener("keypress", (event) => {
    if (event.key === "Enter") {
      sendBtn.click();
    }
  });

  function appendMessage(message, className) {
    const messageElement = document.createElement("div");
    messageElement.classList.add("message", className);
    messageElement.textContent = message;
    chatHistory.appendChild(messageElement);
    chatHistory.scrollTop = chatHistory.scrollHeight;
  }

  function botResponse(userInput) {
    const botMessage = `You said: ${userInput}`;
    setTimeout(() => {
      appendMessage(botMessage, "bot-message");
    }, 1000);
  }
});
