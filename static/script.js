document.getElementById("speak-btn").addEventListener("click", function() {
    fetch("/ask", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({})
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("user-text").innerText = data.response;
        document.getElementById("assistant-text").innerText = "Assistant: Processing response...";
    })
    .catch((error) => {
        console.error("Error:", error);
    });
});
