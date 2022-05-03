var tempDaysWeekdays = [];

let webSocketProtocol = location.protocol == 'https:' ? 'wss' : 'ws';

const chatSocket = new WebSocket(
    `${webSocketProtocol}://${window.location.host}/ws/chat/${chatgroupId}/`
);

// listen event when receive message
chatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data);
    broadcastMessage(data.message, data.username, data.message_type, data.image_caption)
    scrollBottom()
};

// Disconnect to websocket
chatSocket.onclose = function (e) {
    console.error('Chat socket closed unexpectedly');
    console.error(e);
};

document.querySelector('#chat-message-input').focus();

// Send message to websocket
document.querySelector('#chat-message-submit').onclick = function (event) {
    const messageInputDom = document.querySelector('#chat-message-input');
    const message = messageInputDom.value;
    chatSocket.send(JSON.stringify({
        'message': message,
        'message_type': 'text',
        'image_caption': null
    }));
    messageInputDom.value = '';
}

function scrollBottom() {
    let msgbox = document.querySelector(".chat-content")
    msgbox.scrollTop = msgbox.scrollHeight
}

function getTime(msg_time) {
    if (msg_time) {
        // define as Date so we can convert to acceptable date time format
        temp = new Date(msg_time);

        // suffix UTC so it will render as local time when it use toLocalString
        var today = new Date(`${temp.toLocaleString()} UTC`);
    } else {
        var today = new Date();
    }

    // format & render to local time
    let time = today.toLocaleTimeString([], {hour: '2-digit', minute: '2-digit'});
    return time

}

function broadcastMessage(msg, user, msg_type, img_caption, msg_time) {
    // create a new div element
    let newDiv = document.createElement("div");
    // and give it some content
    if (msg_type == 'image') {
        msg = `<img src="${msg}"> <br/> ${img_caption}`;
    }

    if (user == username) {
        newDiv.classList.add('chat');
        var msgInner = `
            <div class="chat-user">
                <a class="avatar m-0">
                    <img src="${userAvatar}" alt="avatar"
                         class="img-45 radius-50 ">
                </a>
                <span class="chat-time mt-1">${getTime(msg_time)}</span>
            </div>
            <div class="chat-detail">
                <div class="chat-message">
                    <p>${msg}</p>
                </div>
            </div>
        `
    } else {
        newDiv.classList.add('chat', 'chat-left');
        var msgInner = `
            <div class="chat-user">
                <a class="avatar m-0">
                    <img src="/static/images/user-2.jpg" alt="avatar"
                         class="img-45 radius-50 ">
                </a>
                <span class="chat-time mt-1">${getTime(msg_time)}</span>
            </div>
            <div class="chat-detail">
                <div class="chat-message">
                    <p>${msg}</p>
                </div>
            </div>
        `
    }

    if (msg_time) {
        showDatesWeekDays(msg_time)
    } else {
        showDatesWeekDays(new Date())
    }

    newDiv.innerHTML = msgInner;

    // add the newly created element and its content into the DOM
    let currentDiv = document.getElementById("new-message-chat");
    let parentDiv = currentDiv.parentNode;
    parentDiv.insertBefore(newDiv, currentDiv);
}

function showDatesWeekDays(date_created) {
    // add the newly created element and its content into the DOM
    date = new Date(date_created)

    if (!tempDaysWeekdays.includes(date.toLocaleDateString())) {
        let newDiv = document.createElement("div");
        let currentDiv = document.getElementById("new-message-chat");
        let parentDiv = currentDiv.parentNode;
        let days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];

        if (date.toDateString() == new Date().toDateString()) {
            // display TODAY in message
            date_weekday = 'TODAY';
        } else if (date > getDateBefore()) {
            // display week day in message
            date_weekday = days[date.getDay()].toUpperCase()
        } else {
            // display date in message
            date_weekday = date.toLocaleDateString();
        }

        newDiv.style.display = "grid";
        newDiv.innerHTML = `<div class="date_weekday">${date_weekday}</div>`
        parentDiv.insertBefore(newDiv, currentDiv);

        tempDaysWeekdays.push(date.toLocaleDateString())
    }

}

function getDateBefore(days = 7) {
    // calculate the last 7 days date
    // 7 (days) * 24 (hours) * 60 (minutes) * 60 (seconds) * 1000 (milliseconds ) = 604800000 or 7 days in milliseconds.
    daysInMs = days * 24 * 60 * 60 * 1000
    return new Date(Date.now() - daysInMs)
}

function loadMessage() {
    fetch(`/chat/history/${chatgroupId}/`)
        .then(response => response.json())
        .then(data => {
            for (let msg of data) {
                broadcastMessage(msg.message, msg.username, msg.message_type, msg.image_caption, msg.date_created)
            }
            scrollBottom()
        })
}

loadMessage()
