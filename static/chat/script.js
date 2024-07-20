document.addEventListener("DOMContentLoaded", () => {
    const chatInput = document.querySelector("#chat-input");
    const sendButton = document.querySelector("#send-btn");
    const chatContainer = document.querySelector(".chat-container");
    const themeButton = document.querySelector("#theme-btn");
    const deleteButton = document.querySelector("#delete-btn");

    const initialHeight = chatInput.scrollHeight;

    const loadDataFromLocalstorage = () => {
        const themeColor = localStorage.getItem("themeColor");
        document.body.classList.toggle("light-mode", themeColor === "light_mode");
        themeButton.innerText = document.body.classList.contains("light-mode") ? "dark_mode" : "light_mode";

        const defaultText = `<div class="default-text">
                                <h1>MTPS BOT</h1>
                                <p>Start a conversation and explore the power of AI.<br> Your chat history will be displayed here.</p>
                            </div>`;
        chatContainer.innerHTML = localStorage.getItem("all-chats") || defaultText;
        chatContainer.scrollTo(0, chatContainer.scrollHeight);
    };

    const createChatElement = (content, className) => {
        const chatDiv = document.createElement("div");
        chatDiv.classList.add("chat", className);
        chatDiv.innerHTML = content;
        return chatDiv;
    };

    const getChatResponse = async (incomingChatDiv, userText) => {
        const formData = new FormData();
        formData.append('csrfmiddlewaretoken', document.querySelector('[name=csrfmiddlewaretoken]').value);
        formData.append('userText', userText);

        try {
            const response = await fetch(document.getElementById('chat-form').action, {
                method: 'POST',
                body: formData
            });
            if (!response.ok) {
                throw new Error(`Error: ${response.status}`);
            }
            const data = await response.json();
            const pElement = document.createElement("p");
            pElement.textContent = data.response;
            incomingChatDiv.querySelector(".typing-animation").remove();
            incomingChatDiv.querySelector(".chat-details").appendChild(pElement);
            localStorage.setItem("all-chats", chatContainer.innerHTML);
            chatContainer.scrollTo(0, chatContainer.scrollHeight);
        } catch (error) {
            console.error("Error fetching chat response:", error);
            const pElement = document.createElement("p");
            pElement.classList.add("error");
            pElement.textContent = "Oops! Something went wrong. Please try again later.";
            incomingChatDiv.querySelector(".typing-animation").remove();
            incomingChatDiv.querySelector(".chat-details").appendChild(pElement);
            chatContainer.scrollTo(0, chatContainer.scrollHeight);
        }
    };

    const handleChat = () => {
        const userText = chatInput.value.trim();
        if (!userText) return;

        chatInput.value = "";
        chatInput.style.height = `${initialHeight}px`;

        const outgoingChatDiv = createChatElement(`<div class="chat-details"><p></p></div>`, "outgoing");
        outgoingChatDiv.querySelector("p").textContent = userText;
        document.querySelector(".default-text")?.remove();
        chatContainer.appendChild(outgoingChatDiv);
        chatContainer.scrollTo(0, chatContainer.scrollHeight);

        setTimeout(() => {
            const incomingChatDiv = createChatElement(`<div class="chat-details"><div class="typing-animation">
                <div class="typing-dot" style="--delay: 0.2s"></div>
                <div class="typing-dot" style="--delay: 0.3s"></div>
                <div class="typing-dot" style="--delay: 0.4s"></div>
            </div></div>`, "incoming");
            chatContainer.appendChild(incomingChatDiv);
            chatContainer.scrollTo(0, chatContainer.scrollHeight);
            getChatResponse(incomingChatDiv, userText);
        }, 500);
    };

    themeButton.addEventListener("click", () => {
        document.body.classList.toggle("light-mode");
        localStorage.setItem("themeColor", themeButton.innerText);
        themeButton.innerText = document.body.classList.contains("light-mode") ? "dark_mode" : "light_mode";
    });

    deleteButton.addEventListener("click", () => {
        if (confirm("Are you sure you want to delete all the chats?")) {
            localStorage.removeItem("all-chats");
            loadDataFromLocalstorage();
        }
    });

    loadDataFromLocalstorage();

    sendButton.addEventListener("click", handleChat);

    chatInput.addEventListener("input", () => {
        chatInput.style.height = `${initialHeight}px`;
        chatInput.style.height = `${chatInput.scrollHeight}px`;
    });

    chatInput.addEventListener("keypress", (e) => {
        if (e.key === "Enter" && !e.shiftKey) {
            e.preventDefault();
            handleChat();
        }
    });
});
