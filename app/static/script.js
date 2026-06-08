let currentInput = "";
let time1 = "";
let operator = "";
let history = "";

const display = document.getElementById("current-input");
const historyDisplay = document.getElementById("history");

function updateDisplay() {
    display.innerText = currentInput || "0с";
    historyDisplay.innerText = history;
}

function appendNumber(num) {
    currentInput += num;
    updateDisplay();
}

function appendUnit(unit) {
    if (currentInput.length > 0 && !currentInput.endsWith("ч") && !currentInput.endsWith("м") && !currentInput.endsWith("с")) {
        currentInput += unit + " ";
        updateDisplay();
    }
}

function clearAll() {
    currentInput = "";
    time1 = "";
    operator = "";
    history = "";
    updateDisplay();
}

function setOperator(op) {
    if (currentInput === "" && time1 === "") return;
    
    if (time1 === "") {
        time1 = currentInput.trim();
        operator = op;
        history = time1 + " " + op;
        currentInput = "";
    } else {
        operator = op;
        history = time1 + " " + op;
    }
    updateDisplay();
}

async function calculate() {
    if (time1 === "" || operator === "" || currentInput === "") return;
    
    const formData = new FormData();
    formData.append("time1", time1);
    formData.append("operator", operator);
    formData.append("operand2", currentInput.trim());
    
    try {
        const response = await fetch("/calculate", {
            method: "POST",
            body: formData
        });
        const data = await response.json();
        
        history = time1 + " " + operator + " " + currentInput.trim() + " =";
        currentInput = data.result;
        time1 = "";
        operator = "";
        updateDisplay();
    } catch (error) {
        display.innerText = "Ошибка";
    }
}
