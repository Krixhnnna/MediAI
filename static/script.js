async function sendMessage() {
    const input = document.getElementById("userInput").value;

    const response = await fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: input })
    });

    const data = await response.json();

    document.getElementById("chatbox").innerHTML += 
        `<p><b>You:</b> ${input}</p>
         <p><b>Bot:</b> ${data.response}</p>`;
}