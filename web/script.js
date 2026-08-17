const display = document.getElementById("display");
const modeButton = document.getElementById("modeButton");
const historyList = document.getElementById("history");

let angleMode = "DEG";
let history = [];

function addToDisplay(value) {
    display.value += value;
    display.focus();
}

function clearDisplay() {
    display.value = "";
    display.focus();
}

function backspace() {
    display.value = display.value.slice(0, -1);
    display.focus();
}

function toggleAngleMode() {
    angleMode = angleMode === "DEG" ? "RAD" : "DEG";
    modeButton.textContent = angleMode;
    display.focus();
}

function formatResult(value) {
    if (!Number.isFinite(value)) {
        throw new Error("Invalid result");
    }

    if (Number.isInteger(value)) {
        return String(value);
    }

    return Number(value.toPrecision(10)).toString();
}

function tokenize(expression) {
    const tokens = [];
    let i = 0;

    while (i < expression.length) {
        const char = expression[i];

        if (/\s/.test(char)) {
            i++;
            continue;
        }

        if (/[0-9.]/.test(char)) {
            let number = "";

            while (
                i < expression.length &&
                /[0-9.]/.test(expression[i])
            ) {
                number += expression[i];
                i++;
            }

            if (
                number === "." ||
                (number.match(/\./g) || []).length > 1
            ) {
                throw new Error("Invalid number");
            }

            tokens.push({
                type: "number",
                value: Number(number)
            });

            continue;
        }

        if (expression.startsWith("pi", i)) {
            tokens.push({
                type: "number",
                value: Math.PI
            });

            i += 2;
            continue;
        }

        if (char === "π") {
            tokens.push({
                type: "number",
                value: Math.PI
            });

            i++;
            continue;
        }

        if (char === "e") {
            tokens.push({
                type: "number",
                value: Math.E
            });

            i++;
            continue;
        }

        if ("+-*/%^()".includes(char)) {
            tokens.push({
                type: "operator",
                value: char
            });

            i++;
            continue;
        }

        const functions = [
            "sqrt",
            "sin",
            "cos",
            "tan",
            "log",
            "ln"
        ];

        let foundFunction = false;

        for (const name of functions) {
            if (expression.startsWith(name, i)) {
                tokens.push({
                    type: "function",
                    value: name
                });

                i += name.length;
                foundFunction = true;
                break;
            }
        }

        if (foundFunction) {
            continue;
        }

        throw new Error("Invalid expression");
    }

    return tokens;
}

function parseExpression(tokens) {
    let position = 0;

    function peek() {
        return tokens[position];
    }

    function consume() {
        return tokens[position++];
    }

    function parsePrimary() {
        const token = peek();

        if (!token) {
            throw new Error("Unexpected end");
        }

        if (
            token.type === "operator" &&
            token.value === "+"
        ) {
            consume();
            return parsePrimary();
        }

        if (
            token.type === "operator" &&
            token.value === "-"
        ) {
            consume();
            return -parsePrimary();
        }

        if (token.type === "number") {
            consume();
            return token.value;
        }

        if (
            token.type === "operator" &&
            token.value === "("
        ) {
            consume();

            const value = parseAdditive();

            const closing = consume();

            if (
                !closing ||
                closing.value !== ")"
            ) {
                throw new Error("Missing )");
            }

            return value;
        }

        if (token.type === "function") {
            const functionName = consume().value;

            const opening = consume();

            if (
                !opening ||
                opening.value !== "("
            ) {
                throw new Error("Expected (");
            }

            const value = parseAdditive();

            const closing = consume();

            if (
                !closing ||
                closing.value !== ")"
            ) {
                throw new Error("Missing )");
            }

            return applyFunction(
                functionName,
                value
            );
        }

        throw new Error("Unexpected token");
    }

    function parsePower() {
        let left = parsePrimary();

        if (
            peek() &&
            peek().value === "^"
        ) {
            consume();

            const right = parsePower();

            left = Math.pow(left, right);
        }

        return left;
    }

    function parseMultiplicative() {
        let left = parsePower();

        while (
            peek() &&
            ["*", "/", "%"].includes(peek().value)
        ) {
            const operator = consume().value;
            const right = parsePower();

            if (
                operator === "/" &&
                right === 0
            ) {
                throw new Error(
                    "Cannot divide by zero"
                );
            }

            if (
                operator === "%" &&
                right === 0
            ) {
                throw new Error(
                    "Cannot divide by zero"
                );
            }

            if (operator === "*") {
                left *= right;
            }

            if (operator === "/") {
                left /= right;
            }

            if (operator === "%") {
                left %= right;
            }
        }

        return left;
    }

    function parseAdditive() {
        let left = parseMultiplicative();

        while (
            peek() &&
            ["+", "-"].includes(peek().value)
        ) {
            const operator = consume().value;
            const right = parseMultiplicative();

            if (operator === "+") {
                left += right;
            } else {
                left -= right;
            }
        }

        return left;
    }

    const result = parseAdditive();

    if (position !== tokens.length) {
        throw new Error("Unexpected token");
    }

    return result;
}

function applyFunction(name, value) {
    switch (name) {
        case "sqrt":
            if (value < 0) {
                throw new Error("Invalid square root");
            }

            return Math.sqrt(value);

        case "log":
            if (value <= 0) {
                throw new Error("Invalid logarithm");
            }

            return Math.log10(value);

        case "ln":
            if (value <= 0) {
                throw new Error("Invalid logarithm");
            }

            return Math.log(value);

        case "sin":
            return Math.sin(
                angleMode === "DEG"
                    ? value * Math.PI / 180
                    : value
            );

        case "cos":
            return Math.cos(
                angleMode === "DEG"
                    ? value * Math.PI / 180
                    : value
            );

        case "tan":
            return Math.tan(
                angleMode === "DEG"
                    ? value * Math.PI / 180
                    : value
            );

        default:
            throw new Error("Unknown function");
    }
}

function evaluateExpression(expression) {
    const tokens = tokenize(expression);

    if (tokens.length === 0) {
        throw new Error("Empty expression");
    }

    return parseExpression(tokens);
}

function calculate() {
    const expression = display.value.trim();

    if (!expression) {
        return;
    }

    try {
        const result = evaluateExpression(expression);
        const formattedResult = formatResult(result);

        addHistory(
            expression,
            formattedResult
        );

        display.value = formattedResult;
        display.focus();

    } catch (error) {
        display.value =
            error.message || "Error";

        display.focus();
    }
}

function addHistory(expression, result) {
    history.push({
        expression,
        result
    });

    renderHistory();
}

function renderHistory() {
    historyList.innerHTML = "";

    for (const item of history) {
        const historyItem =
            document.createElement("div");

        historyItem.className =
            "history-item";

        historyItem.textContent =
            `${item.expression} = ${item.result}`;

        historyItem.addEventListener(
            "dblclick",
            () => {
                display.value =
                    item.expression;

                display.focus();
            }
        );

        historyList.appendChild(historyItem);
    }

    historyList.scrollTop =
        historyList.scrollHeight;
}

function clearHistory() {
    history = [];
    historyList.innerHTML = "";
    display.focus();
}

document
    .querySelectorAll("[data-value]")
    .forEach(button => {
        button.addEventListener(
            "click",
            () => {
                addToDisplay(
                    button.dataset.value
                );
            }
        );
    });

document
    .getElementById("equals")
    .addEventListener(
        "click",
        calculate
    );

document
    .getElementById("clear")
    .addEventListener(
        "click",
        clearDisplay
    );

document
    .getElementById("backspace")
    .addEventListener(
        "click",
        backspace
    );

document
    .getElementById("clearHistory")
    .addEventListener(
        "click",
        clearHistory
    );

modeButton.addEventListener(
    "click",
    toggleAngleMode
);

display.addEventListener(
    "keydown",
    event => {
        if (event.key === "Enter") {
            event.preventDefault();
            calculate();
        }

        if (event.key === "Escape") {
            event.preventDefault();
            clearDisplay();
        }
    }
);

display.focus();