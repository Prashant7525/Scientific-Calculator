# Scientific Calculator

A Python scientific calculator with a modern Tkinter GUI, DEG/RAD modes, calculation history, keyboard support, and a Liquid Glass-inspired design.

## Features

- Basic arithmetic operations
- Power and modulus
- Square root
- Sine, cosine, and tangent
- Base-10 logarithm
- Natural logarithm
- π and e constants
- Parentheses and mathematical expressions
- DEG and RAD angle modes
- Calculation history
- Double-click history reuse
- Keyboard input support
- Enter to calculate
- Escape to clear
- Backspace support
- Input validation
- Result formatting
- Safe expression evaluation
- Windows executable packaging with PyInstaller

## GUI

The calculator uses a Liquid Glass-inspired visual design with:

- Soft layered backgrounds
- Light glass-style panels
- Subtle borders
- Modern button styling
- DEG/RAD mode control
- Color-coded CLEAR HISTORY, CLEAR, and BACKSPACE buttons

## Technologies

- Python 3
- Tkinter
- Math
- AST-based expression evaluation
- PyInstaller

## Project Structure

```text
Scientific-Calculator/
│
├── .gitignore
├── LICENSE
├── README.md
├── calculator.py
├── calculator_engine.py
├── gui_calculator.py
├── gui_layout.py
├── gui_style.py
└── test_engine.py