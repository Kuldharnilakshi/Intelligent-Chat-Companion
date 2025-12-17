function sendMessage() {
    const inputBox = document.getElementById("user-input");
    const chatBox = document.getElementById("chat-box");
    const message = inputBox.value.trim();

    if (!message) return;

    // User message
    chatBox.innerHTML += `<div class="user-msg">${message}</div>`;
    chatBox.scrollTop = chatBox.scrollHeight;
    inputBox.value = "";

    // Typing indicator
    const typingDiv = document.createElement("div");
    typingDiv.className = "bot-msg";
    typingDiv.innerHTML = "Typing...";
    chatBox.appendChild(typingDiv);
    chatBox.scrollTop = chatBox.scrollHeight;

    // Fetch response
    fetch("/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: message })
    })
    .then(response => response.json())
    .then(data => {
        typingDiv.innerHTML = data.answer;
        chatBox.scrollTop = chatBox.scrollHeight;
    });
}

/* 🌙 DARK MODE TOGGLE (GLOBAL FUNCTION) */
function toggleTheme() {
    document.body.classList.toggle("dark");

    const btn = document.getElementById("theme-toggle");
    btn.textContent = document.body.classList.contains("dark") ? "☀️" : "🌙";
}
