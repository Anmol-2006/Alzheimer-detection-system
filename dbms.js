document.addEventListener('DOMContentLoaded', () => {
  const chatBox = document.getElementById('chat-box');
  const userInput = document.getElementById('user-input');
  const sendButton = document.querySelector('.chatbot-container button'); // Assuming the button is the first button inside the container

  function displayMessage(sender, message) {
      const messageDiv = document.createElement('div');
      messageDiv.classList.add('chat-message');
      messageDiv.classList.add(sender); // Add 'user' or 'bot' class for styling
      messageDiv.textContent = `${sender}: ${message}`;
      chatBox.appendChild(messageDiv);
      chatBox.scrollTop = chatBox.scrollHeight; // Scroll to the latest message
  }

  async function sendMessage() {
      const userMessage = userInput.value.trim();
      if (!userMessage) return;

      displayMessage('You', userMessage);
      userInput.value = ''; // Clear the input

      try {
          const response = await fetch('http://127.0.0.1:5000/chat', {
              method: 'POST',
              headers: {
                  'Content-Type': 'application/json',
              },
              body: JSON.stringify({ message: userMessage }),
          });

          if (!response.ok) {
              throw new Error(`HTTP error! status: ${response.status}`);
          }

          const data = await response.json();
          const botResponse = data.response;
          displayMessage('Bot', botResponse);

      } catch (error) {
          console.error('Error sending message:', error);
          displayMessage('Bot', 'Sorry, I encountered an error.');
      }
  }

  sendButton.addEventListener('click', sendMessage);

  userInput.addEventListener('keypress', (event) => {
      if (event.key === 'Enter') {
          sendMessage();
      }
  });

  // Initial bot message (optional)
  displayMessage('Bot', 'Hello! How can I help you today?');
});

document.addEventListener('DOMContentLoaded', function() {
  const animatedText = document.querySelector('.animated-text');
  animatedText.style.animation = 'none'; // Reset animation
  animatedText.offsetHeight; // Trigger reflow to restart
  animatedText.style.animation = null; // Re-apply animation
});
