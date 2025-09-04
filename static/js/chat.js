

const chatContainer = document.getElementById("main");

    function sendMessage() {
      const input = document.getElementById("chat-input");
      const text = input.value.trim();
      if (!text) return;

  // 展示用户消息
      const userMsg = document.createElement("div");
      userMsg.className = "message user";


    // 创建消息文本内容
    const messageText = document.createElement("div");
    messageText.textContent = text;
    userMsg.appendChild(messageText);
    chatContainer.appendChild(userMsg);


 // 创建机器人消息容器（等待回复）
      const botMsg = document.createElement("div");
      botMsg.className = "message-bot";
      chatContainer.appendChild(botMsg);

      input.value = "";

      const sendBtn = document.getElementById("send-button");
      sendBtn.disabled = true;
       $.ajax({
        type: "get",
        url: "/getReply/",
        data: {
          text: text,
        },
           dataType: "json",
        success: function (response) {
            //typeWriterEffect(botMsg, response.reply);
            sendBtn.disabled = false;
        if (response.replyType === "table" && Array.isArray(response.reply)) {
            let data = response.reply;
            if (data.length === 0) {
                botMsg.innerHTML = "<p>没有查询到结果</p>";
                return;
            }

            // 先显示 summary
            let html = "";
            if (response.summary) {
                html += `<p class="summary-text">${response.summary}</p>`;
            }
            html +=renderTable(data);

            botMsg.innerHTML = html;
        }
        else if(response.replyType === "line"|| response.replyType === "bar"|| response.replyType === "pie"|| response.replyType === "scatter"
            && Array.isArray(response.reply)){
            //TODO: 未实现
            let data = response.reply;
            if (data.length === 0) {
                botMsg.innerHTML = "<p>没有查询到结果</p>";
                return;
            }

            // 先显示 summary
            let html = "";
            if (response.summary) {
                html += `<p class="summary-text">${response.summary}</p>`;
            }
            html +=renderTable(data);

            botMsg.innerHTML = html;
        }
        else {
            botMsg.innerHTML = response.reply;
        }
            window.scrollTo({ top: document.body.scrollHeight, behavior: "smooth" });
        },
        error: function (xhr, status, error) {
          botMsg.textContent = "出错了：" + error;
          sendBtn.disabled = false;
        },
      });

      window.scrollTo({ top: document.body.scrollHeight, behavior: "smooth" });

    }
    // 展示机器人消息
    function typeWriterEffect(element, text, speed = 10) {
      let i = 0;
      let currentText = "";
      const interval = setInterval(() => {
        currentText += text[i];
        i++;
        element.innerHTML = currentText;
        window.scrollTo({ top: document.body.scrollHeight, behavior: "smooth" });
        if (i >= text.length) clearInterval(interval);
      }, speed);
    }
   function renderTable(data){
            let html = "";
            let keys = Object.keys(data[0]);
            html += "<table class='result-table'><thead><tr>";
            keys.forEach(k => html += `<th>${k}</th>`);
            html += "</tr></thead><tbody>";

            data.forEach((row, idx) => {
                html += `<tr class='row-${idx % 2}'>`;  // 奇偶行不同背景色
                keys.forEach(k => html += `<td>${row[k]}</td>`);
                html += "</tr>";
            });

            html += "</tbody></table>";
            return html;
        }






    //监听按键，enter发送消息
    document.getElementById("chat-input").addEventListener("keydown", function (e) {
      if (e.key === "Enter" && !e.shiftKey) {
        sendMessage();
        //清空输入框
        e.preventDefault();
        e.stopPropagation();
        e.target.value = "";
        //失去焦点
        e.target.blur();
      }
    });









