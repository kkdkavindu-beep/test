const scrambleInput = document.getElementById("scramble");
const solveBtn = document.getElementById("solveBtn");
const resultPanel = document.getElementById("result");
const errorPanel = document.getElementById("error");

const scrambleOut = document.getElementById("scrambleOut");
const moveCount = document.getElementById("moveCount");
const solutionOut = document.getElementById("solutionOut");
const stepsList = document.getElementById("stepsList");

async function solveScramble() {
  resultPanel.classList.add("hidden");
  errorPanel.classList.add("hidden");

  const response = await fetch("/solve", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ scramble: scrambleInput.value }),
  });

  const data = await response.json();

  if (!response.ok || !data.ok) {
    errorPanel.textContent = data.error || "Unknown error";
    errorPanel.classList.remove("hidden");
    return;
  }

  scrambleOut.textContent = data.scramble;
  moveCount.textContent = String(data.move_count);
  solutionOut.textContent = data.solution;

  stepsList.innerHTML = "";
  data.steps.forEach((step, idx) => {
    const li = document.createElement("li");
    li.textContent = `${idx + 1}. ${step}`;
    stepsList.appendChild(li);
  });

  resultPanel.classList.remove("hidden");
}

solveBtn.addEventListener("click", solveScramble);
