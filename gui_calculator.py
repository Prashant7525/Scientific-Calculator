import tkinter as tk
from calculator_engine import evaluate
from gui_layout import create_layout


angle_mode = "DEG"
history = []


def toggle_angle_mode():
    global angle_mode

    angle_mode = "RAD" if angle_mode == "DEG" else "DEG"
    widgets["mode_button"].config(text=angle_mode)


def add_to_display(value):
    widgets["display"].insert(tk.END, value)
    widgets["display"].focus_set()


def clear_display():
    widgets["display"].delete(0, tk.END)
    widgets["display"].focus_set()


def backspace():
    display = widgets["display"]
    current = display.get()

    if current:
        display.delete(len(current) - 1, tk.END)

    display.focus_set()


def format_result(result):
    if isinstance(result, float):
        if result.is_integer():
            return str(int(result))

        return f"{result:.10g}"

    return str(result)


def add_to_history(expression, result):
    history.append(f"{expression} = {result}")

    history_list = widgets["history_list"]
    history_list.delete(0, tk.END)

    for item in history:
        history_list.insert(tk.END, item)

    history_list.yview_moveto(1)


def calculate():
    display = widgets["display"]
    expression = display.get().strip()

    if not expression:
        return

    try:
        result = evaluate(expression, angle_mode)
        formatted_result = format_result(result)

        add_to_history(expression, formatted_result)

        clear_display()
        display.insert(0, formatted_result)

    except ZeroDivisionError:
        clear_display()
        display.insert(0, "Cannot divide by zero")

    except (ValueError, SyntaxError):
        clear_display()
        display.insert(0, "Error")

    display.focus_set()


def clear_history():
    history.clear()
    widgets["history_list"].delete(0, tk.END)
    widgets["display"].focus_set()


def reuse_history(event=None):
    history_list = widgets["history_list"]
    selection = history_list.curselection()

    if not selection:
        return

    item = history_list.get(selection[0])
    expression = item.rsplit(" = ", 1)[0]

    clear_display()
    widgets["display"].insert(0, expression)
    widgets["display"].focus_set()


def keyboard_input(event):
    if event.keysym in ("Return", "KP_Enter"):
        calculate()
        return "break"

    if event.keysym == "Escape":
        clear_display()
        return "break"

    if event.keysym == "BackSpace":
        backspace()
        return "break"

    if event.char == "^":
        add_to_display("**")
        return "break"


def function_button(name):
    return lambda: add_to_display(name + "(")


def value_button(value):
    return lambda: add_to_display(value)


callbacks = {
    "toggle_angle_mode": toggle_angle_mode,
    "calculate": calculate,
    "clear_display": clear_display,
    "clear_history": clear_history,
    "backspace": backspace,
    "reuse_history": reuse_history,
    "pi": lambda: add_to_display("pi"),
    "e": lambda: add_to_display("e"),
    "power": lambda: add_to_display("**"),
    "function": function_button,
    "value": value_button
}


window = tk.Tk()
window.title("Scientific Calculator")
window.geometry("600x800")
window.resizable(False, False)


widgets = create_layout(
    window,
    angle_mode,
    callbacks
)


widgets["display"].focus_set()
widgets["display"].bind(
    "<Key>",
    keyboard_input
)


window.mainloop()