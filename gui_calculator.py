import tkinter as tk
from calculator_engine import evaluate


window = tk.Tk()
window.title("Scientific Calculator v2.2")
window.geometry("500x780")
window.resizable(False, False)

angle_mode = "DEG"
history = []


def toggle_angle_mode():
    global angle_mode

    angle_mode = "RAD" if angle_mode == "DEG" else "DEG"
    mode_button.config(text=angle_mode)


def add_to_display(value):
    display.insert(tk.END, value)


def clear_display():
    display.delete(0, tk.END)


def backspace():
    current = display.get()

    if current:
        display.delete(len(current) - 1, tk.END)


def add_to_history(expression, result):
    history.append(f"{expression} = {result}")

    history_list.delete(0, tk.END)

    for item in history:
        history_list.insert(tk.END, item)


def calculate():
    expression = display.get().strip()

    if not expression:
        return

    try:
        result = evaluate(expression, angle_mode)

        add_to_history(expression, result)

        clear_display()
        display.insert(0, str(result))

    except ZeroDivisionError:
        clear_display()
        display.insert(0, "Cannot divide by zero")

    except (ValueError, SyntaxError):
        clear_display()
        display.insert(0, "Error")


def clear_history():
    history.clear()
    history_list.delete(0, tk.END)


def reuse_history(event):
    selection = history_list.curselection()

    if not selection:
        return

    item = history_list.get(selection[0])
    expression = item.split(" = ")[0]

    clear_display()
    display.insert(0, expression)


def create_button(parent, text, command):
    button = tk.Button(
        parent,
        text=text,
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


history_label = tk.Label(
    window,
    text="Calculation History",
    font=("Arial", 13),
    anchor="w"
)

history_label.pack(
    fill="x",
    padx=10,
    pady=(5, 0)
)


history_frame = tk.Frame(window)
history_frame.pack(
    fill="both",
    padx=10,
    pady=5
)


history_list = tk.Listbox(
    history_frame,
    font=("Arial", 12),
    height=5
)

history_list.pack(
    side="left",
    fill="both",
    expand=True
)


history_scrollbar = tk.Scrollbar(
    history_frame,
    command=history_list.yview
)

history_scrollbar.pack(
    side="right",
    fill="y"
)

history_list.config(
    yscrollcommand=history_scrollbar.set
)

history_list.bind(
    "<Double-Button-1>",
    reuse_history
)


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

        create_button(
            frame,
            button_text,
            command
        )


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

        create_button(
            frame,
            button_text,
            command
        )


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


clear_history_button = tk.Button(
    control_frame,
    text="CLEAR HISTORY",
    font=("Arial", 15),
    command=clear_history
)

clear_history_button.pack(
    side="left",
    expand=True,
    fill="both",
    padx=2
)


window.mainloop()