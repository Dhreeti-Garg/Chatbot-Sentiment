const chatBox = document.getElementById("chatBox");
const inputMsg = document.getElementById("inputMsg");
const sendBtn = document.getElementById("sendBtn");
const endBtn = document.getElementById("endBtn");
const resetBtn = document.getElementById("resetBtn");
const typingEl = document.getElementById("typing");

let trendChart = null;
let scores = []; // numeric scores [-1..1]

// escape HTML
function escapeHtml(unsafe) {
  return unsafe.replace(/[&<"']/g, function (m) {
    return { "&": "&amp;", "<": "&lt;", '"': "&quot;", "'": "&#039;" }[m];
  });
}

function appendMessage(text, who = "bot", sentiment = null) {
  const d = document.createElement("div");
  d.classList.add("msg", who === "user" ? "user" : "bot");
  let label = "";
  if (sentiment) {
    const emoji =
      sentiment === "Positive" ? "😊" : sentiment === "Negative" ? "😟" : "😐";
    label = ` <span class="label">${emoji} ${sentiment}</span>`;
  }
  if (who === "user") {
    d.innerHTML = `<strong>You:</strong> ${escapeHtml(text)}`;
  } else {
    d.innerHTML = `<strong>Lumi:</strong> ${escapeHtml(text)}${label}`;
  }
  chatBox.appendChild(d);
  chatBox.scrollTop = chatBox.scrollHeight;
}

function showTyping(show = true) {
  typingEl.style.display = show ? "block" : "none";
}

async function sendMessage() {
  const text = inputMsg.value.trim();
  if (!text) return;
  appendMessage(text, "user");
  inputMsg.value = "";
  showTyping(true);
  try {
    const res = await fetch("/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: text }),
    });
    const data = await res.json();
    appendMessage(data.bot, "bot", data.sentiment);
    scores.push(data.score);
    updateStatsAndChart();
  } catch (err) {
    console.error(err);
    appendMessage("Sorry — unable to contact server.", "bot");
  } finally {
    showTyping(false);
  }
}

sendBtn.addEventListener("click", sendMessage);
inputMsg.addEventListener("keydown", function (e) {
  if (e.key === "Enter") sendMessage();
});

endBtn.addEventListener("click", async function () {
  try {
    const res = await fetch("/sentiment");
    const data = await res.json();
    const rep = document.getElementById("reportText");
    rep.innerHTML = `<p><strong>Overall Mood:</strong> ${
      data.overall_label
    } (avg ${data.average_score})</p>
      <p><strong>Counts:</strong> Positive ${data.stats.positive}, Neutral ${
      data.stats.neutral
    }, Negative ${data.stats.negative}</p>
      <p><strong>Trend:</strong> ${generateTrendSummary(scores)}</p>`;
    document.getElementById("finalReport").style.display = "block";
  } catch (e) {
    console.error(e);
  }
});

resetBtn.addEventListener("click", async function () {
  await fetch("/reset", { method: "POST" });
  chatBox.innerHTML = "";
  scores = [];
  updateStatsAndChart();
  document.getElementById("finalReport").style.display = "none";
});

// update stats & chart
function updateStatsAndChart() {
  const total = scores.length;
  let pos = 0,
    neu = 0,
    neg = 0;
  scores.forEach((s) => {
    if (s >= 0.05) pos++;
    else if (s <= -0.05) neg++;
    else neu++;
  });
  document.getElementById("statTotal").innerText = total;
  document.getElementById("statPos").innerText = pos;
  document.getElementById("statNeu").innerText = neu;
  document.getElementById("statNeg").innerText = neg;

  // chart
  const ctx = document.getElementById("trendChart").getContext("2d");
  const labels = scores.map((_, i) => i + 1);
  const data = scores.map((s) => parseFloat(s));
  if (trendChart) {
    trendChart.data.labels = labels;
    trendChart.data.datasets[0].data = data;
    trendChart.update();
  } else {
    trendChart = new Chart(ctx, {
      type: "line",
      data: {
        labels: labels,
        datasets: [
          {
            label: "Sentiment score",
            data: data,
            borderColor: "rgba(124,97,255,0.95)",
            backgroundColor: "rgba(0,194,255,0.06)",
            tension: 0.25,
            pointRadius: 4,
          },
        ],
      },
      options: {
        scales: { y: { min: -1, max: 1, ticks: { stepSize: 0.5 } } },
        plugins: { legend: { display: false } },
        maintainAspectRatio: false,
      },
    });
  }
}

function generateTrendSummary(arr) {
  if (!arr.length) return "No messages yet.";
  const first = arr[0],
    last = arr[arr.length - 1];
  if (last - first > 0.1) return "Mood improved over the conversation.";
  if (first - last > 0.1) return "Mood declined over the conversation.";
  return "Mood was relatively stable.";
}

// init - load existing conversation
async function init() {
  try {
    const res = await fetch("/sentiment");
    const data = await res.json();
    data.conversation.forEach((c) => {
      appendMessage(c.user, "user");
      appendMessage(c.bot, "bot", c.sentiment);
      scores.push(c.score);
    });
    updateStatsAndChart();
  } catch (e) {
    console.error(e);
  }
}
init();
