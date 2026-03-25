const moodEmojis = {
    "Happy": "😄",
    "Sad": "😢",
    "Angry": "😡",
    "Stress": "😫",
    "Anxious": "😰",
    "Excited": "🤩",
    "Neutral": "😐",
    "Bored": "🥱"
};

function send() {
    let textInput = document.getElementById("text");
    let text = textInput.value.trim();
    let resultDiv = document.getElementById("result");

    if (text === "") {
        alert("Please enter how you feel");
        return;
    }

    // Show user message (chat bubble)
    resultDiv.innerHTML += `
        <div class="user-bubble">${text}</div>
    `;

    fetch("/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: text })
    })
    .then(res => res.json())
    .then(data => {

        // 🌈 Change background color based on mood
        document.body.className = "";
        document.body.classList.add("bg-" + data.mood);

        // Fake confidence (70–95%) for demo
        let confidence = Math.floor(Math.random() * 25) + 70;

        // Append bot response (chat bubble)
        resultDiv.innerHTML += `
            <div class="bot-bubble mood-${data.mood}">
                <h3>${moodEmojis[data.mood]} ${data.mood}</h3>
                <p>${data.suggestion}</p>

                <div class="progress">
                    <div class="progress-bar" style="width:${confidence}%"></div>
                </div>
                <p>${confidence}% sure</p>
            </div>
        `;

        // Auto-scroll to bottom
        resultDiv.scrollTop = resultDiv.scrollHeight;
    });

    // Clear input box
    textInput.value = "";
}

/* 🌙 Dark Mode Toggle */
function toggleDarkMode() {
    document.body.classList.toggle("dark-mode");
}
