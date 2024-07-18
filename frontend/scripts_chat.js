let chatHistory = [];
let currentChatIndex = -1;

function sendMessage() {
  const userInput = document.getElementById("user-input");
  const chatBox = document.getElementById("chat-box");

  const userMessage = userInput.value;
  if (userMessage.trim() === "") return;

  // Append user message to chat box
  const userMessageElement = document.createElement("div");
  userMessageElement.textContent = userMessage;
  userMessageElement.className = "user-message";
  chatBox.appendChild(userMessageElement);

  // Clear the input field
  userInput.value = "";

  // Simulate a bot response
  const botMessageElement = document.createElement("div");
  botMessageElement.textContent = "This is a simulated response from ChatGPT.";
  botMessageElement.className = "bot-message";
  chatBox.appendChild(botMessageElement);

  // Scroll to the bottom of the chat box
  chatBox.scrollTop = chatBox.scrollHeight;

  // Save the conversation to chat history
  if (currentChatIndex === -1) {
    saveToHistory(userMessage, botMessageElement.textContent);
  } else {
    // Append to existing conversation
    chatHistory[currentChatIndex].conversation.push({
      userMessage: userMessage,
      botMessage: botMessageElement.textContent,
    });
  }
}

function saveToHistory(userMessage, botMessage) {
  const chatItem = {
    conversation: [{ userMessage: userMessage, botMessage: botMessage }],
  };
  chatHistory.push(chatItem);
  currentChatIndex = chatHistory.length - 1;
  updateChatHistory();
}

function updateChatHistory() {
  const historyList = document.getElementById("chat-history");
  historyList.innerHTML = "";

  chatHistory.forEach((chatItem, index) => {
    const chatHistoryElement = document.createElement("div");
    chatHistoryElement.textContent = `Chat ${index + 1}`;
    chatHistoryElement.className = "chat-history-item";
    chatHistoryElement.onclick = () => loadChat(index);

    if (index === currentChatIndex) {
      chatHistoryElement.classList.add("active");
    }

    historyList.appendChild(chatHistoryElement);
  });
}

function loadChat(index) {
  currentChatIndex = index;
  const chatBox = document.getElementById("chat-box");
  chatBox.innerHTML = "";

  const chatItem = chatHistory[index];
  chatItem.conversation.forEach((message) => {
    const userMessageElement = document.createElement("div");
    userMessageElement.textContent = message.userMessage;
    userMessageElement.className = "user-message";
    chatBox.appendChild(userMessageElement);

    const botMessageElement = document.createElement("div");
    botMessageElement.textContent = message.botMessage;
    botMessageElement.className = "bot-message";
    chatBox.appendChild(botMessageElement);
  });

  updateChatHistory();
}

function startNewChat() {
  currentChatIndex = -1;
  const chatBox = document.getElementById("chat-box");
  chatBox.innerHTML = "";
  updateChatHistory();
}

function handleKeyPress(event) {
  if (event.key === "Enter") {
    sendMessage();
  }
}
