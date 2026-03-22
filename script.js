async function uploadPDF() {
    const file = document.getElementById("pdfFile").files[0];
    let formData = new FormData();
    formData.append("file", file);

    await fetch("http://127.0.0.1:8000/upload/", {
        method: "POST",
        body: formData
    });

    alert("Book uploaded!");
}

async function ask() {
    const q = document.getElementById("question").value;
    const chatBox = document.getElementById("chatBox");

    chatBox.innerHTML += `<div class="user">${q}</div>`;

    try {
        const res = await fetch(`http://127.0.0.1:8000/ask/?q=${q}`);
        const data = await res.json();

        chatBox.innerHTML += `<div class="bot">${data.answer}</div>`;
    } catch (error) {
        chatBox.innerHTML += `<div class="bot">❌ Error connecting to server</div>`;
    }
}