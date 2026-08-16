import tkinter as tk
from calculator_engine import evaluate


# -----------------------------
# Main Window
# -----------------------------

window = tk.Tk()
window.title("Scientific Calculator v2.1")
window.geometry("500x700")
window.resizable(False, False)


# -----------------------------
# Angle Mode
# -----------------------------

angle_mode = "DEG"


def toggle_angle_mode():
    global angle_mode

    if angle_mode == "DEG":
        angle_mode = "RAD"
    else:
        angle_mode = "DEG"

    mode_button.config(text=angle_mode)


# -----------------------------
# Display
# -----------------------------

display = tk.Entry(
    window,
    font=("Arial", 24),
    justify="right",
    bd=10,
    relief=tk.RIDGE
)

display.pack(
    fill="x",
    padx=10,
    pady=10,
    ipady=10
)


# -----------------------------
# Display Functions
# -----------------------------

def add_to_display(value):
    display.insert(tk.END, value)


def clear_display():
    display.delete(0, tk.END)


def backspace():
    current = display.get()

    if current:
        display.delete(len(current) - 1, tk.END)


def calculate():
    expression = display.get()

    try:
        result = evaluate(
            expression,
            angle_mode
        )

        clear_display()
        display.insert(0, str(result))

    except ZeroDivisionError:
        clear_display()
        display.insert(0, "Cannot divide by zero")

    except (ValueError, SyntaxError):
        clear_display()
        display.insert(0, "Error")


# -----------------------------
# Mode Button
# -----------------------------

mode_frame = tk.Frame(window)
mode_frame.pack(
    fill="both",
    padx=10,
    pady=2
)

mode_button = tk.Button(
    mode_frame,
    text=angle_mode,
    font=("Arial", 14),
    command=toggle_angle_mode
)

mode_button.pack(
    side="right",
    padx=2,
    pady=2
)


# -----------------------------
# Scientific Buttons
# -----------------------------

scientific_buttons = [
    ["sin", "cos", "tan", "sqrt"],
    ["log", "ln", "π", "e"],
    ["(", ")", "**", "%"]
]


for row in scientific_buttons:

    frame = tk.Frame(window)
    frame.pack(
        expand=True,
        fill="both"
    )

    for button_text in row:

        if button_text == "π":
            command = lambda: add_to_display("pi")

        elif button_text == "e":
            command = lambda: add_to_display("e")

        elif button_text in [
            "sin",
            "cos",
            "tan",
            "sqrt",
            "log",
            "ln"
        ]:
            command = lambda value=button_text: add_to_display(
                value + "("
            )

        else:
            command = lambda value=button_text: add_to_display(
                value
            )

        button = tk.Button(
            frame,
            text=button_text,
            font=("Arial", 15),
            command=command
        )

        button.pack(
            side="left",
            expand=True,
            fill="both",
            padx=2,
            pady=2
        )


# -----------------------------
# Number Buttons
# -----------------------------

number_buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"]
]


for row in number_buttons:

    frame = tk.Frame(window)
    frame.pack(
        expand=True,
        fill="both"
    )

    for button_text in row:

        if button_text == "=":
            command = calculate

        else:
            command = lambda value=button_text: add_to_display(
                value
            )

        button = tk.Button(
            frame,
            text=button_text,
            font=("Arial", 15),
            command=command
        )

        button.pack(
            side="left",
            expand=True,
            fill="both",
            padx=2,
            pady=2
        )


# -----------------------------
# Control Buttons
# -----------------------------

control_frame = tk.Frame(window)
control_frame.pack(
    fill="both",
    padx=10,
    pady=5
)


clear_button = tk.Button(
    control_frame,
    text="CLEAR",
    font=("Arial", 15),
    command=clear_display
)

clear_button.pack(
    side="left",
    expand=True,
    fill="both",
    padx=2
)


backspace_button = tk.Button(
    control_frame,
    text="⌫",
    font=("Arial", 15),
    command=backspace
)

backspace_button.pack(
    side="left",
    expand=True,
    fill="both",
    padx=2
)


# -----------------------------
# Start Application
# -----------------------------

window.mainloop()