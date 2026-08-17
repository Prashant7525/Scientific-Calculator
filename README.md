# Scientific Calculator

A Python scientific calculator with a modern Tkinter desktop GUI and a responsive browser-based web edition.

The project includes DEG/RAD modes, scientific functions, calculation history, keyboard support, safe expression evaluation, a Liquid Glass-inspired interface, automated tests, Windows executable packaging, and GitHub Pages deployment.

## Live Demo

Try the web version online:

**[Scientific Calculator Web App](https://Prashant7525.github.io/Scientific-Calculator/)**

The web edition is deployed using GitHub Pages.

## Features

- Scientific calculator operations
- Addition, subtraction, multiplication, and division
- Power operations
- Modulus
- Square root
- Base-10 logarithm
- Natural logarithm
- π and e constants
- Parentheses and mathematical expressions
- DEG and RAD angle modes
- Calculation history
- Double-click history reuse
- Keyboard input support
- Enter, Escape, and Backspace controls
- Input validation
- Result formatting
- Safe expression evaluation
- Liquid Glass-inspired interface
- Responsive web interface
- Automated calculator engine tests
- Windows executable packaging with PyInstaller
- Standalone Windows `.exe`
- GitHub Pages web deployment

## Project Structure

```text
Scientific-Calculator/
│
├── calculator.py
│       Command-line calculator
│
├── calculator_engine.py
│       Core mathematical expression engine
│
├── gui_calculator.py
│       Main desktop GUI application logic
│
├── gui_layout.py
│       Desktop GUI layout and widget creation
│
├── gui_style.py
│       Desktop GUI theme and styling
│
├── test_engine.py
│       Automated calculator engine tests
│
├── docs/
│   ├── index.html
│   │       Web calculator structure
│   │
│   ├── style.css
│   │       Web calculator styling
│   │
│   └── script.js
│           Web calculator functionality
│
├── .gitignore
│       Git ignored files
│
├── LICENSE
│       MIT License
│
└── README.md
        Project documentation
```

## Requirements

### Desktop Version

- Windows, macOS, or Linux
- Python 3
- Tkinter

Tkinter is included with most standard Python installations.

### Web Version

No Python installation is required.

The web calculator runs directly in a modern web browser.

## Running the Desktop Calculator

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

A standalone Windows executable is available from the GitHub Release.

Download the latest Windows `.exe` from:

**[Scientific Calculator Releases](https://github.com/Prashant7525/Scientific-Calculator/releases)**

The executable can be run without installing Python.

### Build the Windows Executable Yourself

Install PyInstaller:

```bash
python -m pip install -U pyinstaller
```

Build the executable:

```bash
pyinstaller --onefile --windowed --name "Scientific Calculator" gui_calculator.py
```

The executable will be created at:

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

## Web Edition

The web edition is located in the `docs/` directory.

It uses:

- HTML
- CSS
- JavaScript
- A custom client-side expression parser

The web interface provides a responsive Liquid Glass-inspired calculator experience directly in the browser.

### Run the Web Version Locally

Open:

```text
docs/index.html
```

in a modern web browser.

Alternatively, use a local development server:

```bash
python -m http.server 8000 --directory docs
```

Then open:

```text
http://localhost:8000
```

## GitHub Pages Deployment

The web edition is deployed using GitHub Pages.

Live website:

**[Scientific Calculator Web App](https://Prashant7525.github.io/Scientific-Calculator/)**

GitHub Pages publishes the contents of:

```text
docs/
```

The production site is served from the `main` branch after the v4.0 web edition is merged.

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

Constants:

```text
π
e
```

Examples:

```text
2 + 3 * 4
```

```text
2 ^ 3
```

```text
sqrt(25)
```

```text
log(100)
```

```text
ln(e)
```

```text
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
```

```text
sqrt(25) = 5
```

```text
sin(90) = 1
```

Double-click a history entry to reuse its expression.

Use:

```text
CLEAR HISTORY
```

to remove all stored calculations.

## Project Versions

### v4.0.0 — Web Edition

- Added browser-based scientific calculator
- Added responsive Liquid Glass-inspired web interface
- Added DEG/RAD support
- Added calculation history
- Added keyboard support
- Added scientific functions
- Added safe client-side expression parser
- Added responsive mobile layout
- Added GitHub Pages deployment
- Added live web demo

### v3.0.0 — Desktop Edition

- Refactored GUI architecture
- Separated GUI logic, layout, and styling
- Added Liquid Glass-inspired Tkinter interface
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

## Links

- **Live Web App:** https://Prashant7525.github.io/Scientific-Calculator/
- **GitHub Repository:** https://github.com/Prashant7525/Scientific-Calculator
- **Windows Releases:** https://github.com/Prashant7525/Scientific-Calculator/releases
