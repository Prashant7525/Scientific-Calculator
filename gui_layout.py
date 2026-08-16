import tkinter as tk

from gui_style import (
    BG,
    PANEL,
    BUTTON,
    BUTTON_ACTIVE,
    TEXT,
    SECONDARY,
    BORDER,
    RED,
    RED_ACTIVE,
    YELLOW,
    YELLOW_ACTIVE,
    BLUE,
    BLUE_ACTIVE,
    TITLE_FONT,
    DISPLAY_FONT,
    HISTORY_FONT,
    HISTORY_TITLE_FONT,
    SCIENTIFIC_FONT,
    NUMBER_FONT,
    CONTROL_FONT,
    BACKSPACE_FONT,
    MODE_FONT
)


def create_button(parent, text, command, font):
    return tk.Button(
        parent,
        text=text,
        command=command,
        font=font,
        bg=BUTTON,
        fg=TEXT,
        activebackground=BUTTON_ACTIVE,
        activeforeground=TEXT,
        bd=0,
        relief=tk.FLAT,
        highlightthickness=1,
        highlightbackground=BORDER,
        highlightcolor=BORDER
    )


def create_layout(window, angle_mode, callbacks):
    window.configure(bg=BG)

    main_frame = tk.Frame(
        window,
        bg=BG
    )

    main_frame.pack(
        fill="both",
        expand=True,
        padx=12,
        pady=10
    )

    header = tk.Frame(
        main_frame,
        bg=BG
    )

    header.pack(
        fill="x",
        pady=(2, 8)
    )

    title = tk.Label(
        header,
        text="SCIENTIFIC CALCULATOR",
        font=TITLE_FONT,
        bg=BG,
        fg=TEXT
    )

    title.pack(side="left")

    mode_button = tk.Button(
        header,
        text=angle_mode,
        font=MODE_FONT,
        width=6,
        command=callbacks["toggle_angle_mode"],
        bg=PANEL,
        fg=TEXT,
        activebackground=BUTTON_ACTIVE,
        activeforeground=TEXT,
        bd=0,
        relief=tk.FLAT,
        highlightthickness=1,
        highlightbackground=BORDER
    )

    mode_button.pack(
        side="right",
        padx=3
    )

    display_frame = tk.Frame(
        main_frame,
        bg=PANEL,
        highlightthickness=1,
        highlightbackground=BORDER
    )

    display_frame.pack(
        fill="x",
        pady=(0, 10)
    )

    display = tk.Entry(
        display_frame,
        font=DISPLAY_FONT,
        justify="right",
        bd=0,
        relief=tk.FLAT,
        bg=PANEL,
        fg=TEXT,
        insertbackground=TEXT
    )

    display.pack(
        fill="x",
        ipady=12,
        padx=12,
        pady=8
    )

    history_title = tk.Label(
        main_frame,
        text="Calculation History",
        font=HISTORY_TITLE_FONT,
        anchor="w",
        bg=BG,
        fg=SECONDARY
    )

    history_title.pack(
        fill="x",
        pady=(0, 4)
    )

    history_frame = tk.Frame(
        main_frame,
        bg=PANEL,
        highlightthickness=1,
        highlightbackground=BORDER
    )

    history_frame.pack(
        fill="x",
        pady=(0, 10)
    )

    history_list = tk.Listbox(
        history_frame,
        font=HISTORY_FONT,
        height=4,
        bd=0,
        relief=tk.FLAT,
        bg=PANEL,
        fg=TEXT,
        selectbackground=BLUE,
        selectforeground="white"
    )

    history_list.pack(
        side="left",
        fill="both",
        expand=True,
        padx=6,
        pady=5
    )

    history_scrollbar = tk.Scrollbar(
        history_frame,
        command=history_list.yview
    )

    history_scrollbar.pack(
        side="right",
        fill="y",
        padx=(0, 4),
        pady=5
    )

    history_list.config(
        yscrollcommand=history_scrollbar.set
    )

    history_list.bind(
        "<Double-Button-1>",
        callbacks["reuse_history"]
    )

    button_area = tk.Frame(
        main_frame,
        bg=BG
    )

    button_area.pack(
        fill="both",
        expand=True
    )

    for column in range(4):
        button_area.columnconfigure(
            column,
            weight=1,
            uniform="buttons"
        )

    for row in range(7):
        button_area.rowconfigure(
            row,
            weight=1,
            uniform="buttons"
        )

    scientific_buttons = [
        ["sin", "cos", "tan", "sqrt"],
        ["log", "ln", "π", "e"],
        ["(", ")", "^", "%"]
    ]

    for row_index, row in enumerate(scientific_buttons):

        for column_index, button_text in enumerate(row):

            if button_text == "π":
                command = callbacks["pi"]

            elif button_text == "e":
                command = callbacks["e"]

            elif button_text == "^":
                command = callbacks["power"]

            elif button_text in [
                "sin",
                "cos",
                "tan",
                "sqrt",
                "log",
                "ln"
            ]:
                command = callbacks["function"](button_text)

            else:
                command = callbacks["value"](button_text)

            button = create_button(
                button_area,
                button_text,
                command,
                SCIENTIFIC_FONT
            )

            button.grid(
                row=row_index,
                column=column_index,
                sticky="nsew",
                padx=3,
                pady=3
            )

    number_buttons = [
        ["7", "8", "9", "/"],
        ["4", "5", "6", "*"],
        ["1", "2", "3", "-"],
        ["0", ".", "=", "+"]
    ]

    for row_offset, row in enumerate(number_buttons, start=3):

        for column_index, button_text in enumerate(row):

            if button_text == "=":
                command = callbacks["calculate"]

            else:
                command = callbacks["value"](button_text)

            button = create_button(
                button_area,
                button_text,
                command,
                NUMBER_FONT
            )

            button.grid(
                row=row_offset,
                column=column_index,
                sticky="nsew",
                padx=3,
                pady=3
            )

    control_frame = tk.Frame(
        main_frame,
        bg=BG
    )

    control_frame.pack(
        fill="x",
        pady=(7, 0)
    )

    for column in range(3):
        control_frame.columnconfigure(
            column,
            weight=1,
            uniform="controls"
        )

    clear_history_button = tk.Button(
        control_frame,
        text="CLEAR HISTORY",
        font=CONTROL_FONT,
        height=2,
        command=callbacks["clear_history"],
        bg=RED,
        fg="white",
        activebackground=RED_ACTIVE,
        activeforeground="white",
        bd=0,
        relief=tk.FLAT
    )

    clear_history_button.grid(
        row=0,
        column=0,
        sticky="nsew",
        padx=3
    )

    clear_button = tk.Button(
        control_frame,
        text="CLEAR",
        font=CONTROL_FONT,
        height=2,
        command=callbacks["clear_display"],
        bg=YELLOW,
        fg=TEXT,
        activebackground=YELLOW_ACTIVE,
        activeforeground=TEXT,
        bd=0,
        relief=tk.FLAT
    )

    clear_button.grid(
        row=0,
        column=1,
        sticky="nsew",
        padx=3
    )

    backspace_button = tk.Button(
        control_frame,
        text="⌫",
        font=BACKSPACE_FONT,
        height=2,
        command=callbacks["backspace"],
        bg=BLUE,
        fg="white",
        activebackground=BLUE_ACTIVE,
        activeforeground="white",
        bd=0,
        relief=tk.FLAT
    )

    backspace_button.grid(
        row=0,
        column=2,
        sticky="nsew",
        padx=3
    )

    return {
        "display": display,
        "mode_button": mode_button,
        "history_list": history_list
    }