# Scientific Calculator

A Python scientific calculator with a modern Tkinter GUI, DEG/RAD modes, calculation history, keyboard support, and a Liquid Glass-inspired design.

## Download Windows App

**[Download Scientific Calculator v3.0.0 for Windows](https://github.com/Prashant7525/Scientific-Calculator/releases/tag/v3.0.0)**

Download the standalone Windows executable from the GitHub Release. No Python installation is required.

**File:** `Scientific.Calculator.exe`

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
```

### File Description

| File | Purpose |
|---|---|
| `calculator.py` | Command-line calculator |
| `calculator_engine.py` | Mathematical expression engine |
| `gui_calculator.py` | Main GUI application logic |
| `gui_layout.py` | GUI layout and widgets |
| `gui_style.py` | GUI theme and styling |
| `test_engine.py` | Calculator engine tests |
| `.gitignore` | Git ignored files |
| `LICENSE` | MIT License |

## Requirements

- Windows, macOS, or Linux
- Python 3
- Tkinter

Tkinter is included with most standard Python installations.

## Running the Calculator

Clone the repository:

```bash
git clone https://github.com/Prashant7525/Scientific-Calculator.git
```

Open the project directory:

```bash
cd Scientific-Calculator
```

Run the graphical calculator:

```bash
python gui_calculator.py
```

Run the command-line calculator:

```bash
python calculator.py
```

## Running Tests

Run the calculator engine tests:

```bash
python test_engine.py
```

A successful test run displays:

```text
All calculator engine tests passed.
```

## Windows Executable

A standalone Windows executable can be created using PyInstaller.

Install PyInstaller:

```bash
python -m pip install -U pyinstaller
```

Build the executable:

```bash
pyinstaller --onefile --windowed --name "Scientific Calculator" gui_calculator.py
```

The executable will be created in:

```text
dist/Scientific Calculator.exe
```

The generated executable can be run without installing Python.

### PyInstaller Build Files

The following generated files and folders are intentionally excluded from Git:

```text
build/
dist/
*.spec
```

## Keyboard Controls

| Key | Action |
|---|---|
| `0-9` | Enter numbers |
| `+` `-` `*` `/` | Basic operators |
| `^` | Power |
| `%` | Modulus |
| `(` `)` | Parentheses |
| `Enter` | Calculate |
| `Backspace` | Delete last character |
| `Escape` | Clear display |

## Scientific Functions

The calculator supports:

```text
sin()
cos()
tan()
sqrt()
log()
ln()
```

### Constants

```text
π
e
```

### Examples

```text
2 + 3 * 4
2 ^ 3
sqrt(25)
log(100)
ln(e)
sin(90)
```

## Angle Modes

The calculator supports two angle modes.

### DEG

Calculations use degrees.

Example:

```text
sin(90) = 1
```

### RAD

Calculations use radians.

Example:

```text
sin(pi / 2) = 1
```

Use the DEG/RAD button to switch between modes.

## Calculation History

The calculator automatically stores completed calculations in the history panel.

Example:

```text
2 + 3 * 4 = 14
sqrt(25) = 5
sin(90) = 1
```

Double-click a history entry to reuse its expression.

Use:

```text
CLEAR HISTORY
```

to remove all stored calculations.

## Project Versions

### v3.0.0

- Refactored GUI architecture
- Separated GUI logic, layout, and styling
- Added Liquid Glass-inspired interface
- Added project documentation
- Added MIT License
- Added automated engine tests
- Improved project structure
- Added PyInstaller packaging support
- Added Windows executable release

### v2.3

- Added keyboard support
- Added Enter, Escape, and Backspace controls
- Added result formatting
- Added `^` power button

### v2.2

- Added calculation history
- Added history reuse

### v2.1

- Added DEG/RAD mode

### v2.0

- Added Tkinter scientific GUI
- Added dedicated calculation engine

### v1.2

- Added input validation

### v1.1

- Added scientific operations

### v1.0

- Initial calculator release

## License

This project is licensed under the MIT License.

See the [LICENSE](LICENSE) file for details.

## Author

**Prashant Kumar**

GitHub: [Prashant7525](https://github.com/Prashant7525)
