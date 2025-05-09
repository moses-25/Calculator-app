# Calculator Project

This project contains two implementations of a calculator: a web-based calculator using HTML, CSS, and JavaScript, and a desktop GUI calculator built with Python and Tkinter.

## Files

### 1. `Calculator.html`
- A responsive web-based calculator with a clean and modern design.
- Features:
  - Basic arithmetic operations: addition, subtraction, multiplication, and division.
  - Clear button to reset the display.
  - Styled using CSS for an intuitive user interface.
- JavaScript functions:
  - `appendValue(value)`: Appends the clicked button's value to the display.
  - `calculate()`: Evaluates the expression in the display.
  - `clearDisplay()`: Clears the display.

### 2. `Calculator_2.py`
- A desktop calculator application built with Python's Tkinter library.
- Features:
  - Basic arithmetic operations and additional functionalities like parentheses and percentage.
  - Clear button to reset the input.
  - Error handling for invalid expressions.
- Key components:
  - `show(value)`: Updates the display with the clicked button's value.
  - `clear()`: Clears the input field.
  - `solve()`: Evaluates the entered expression and displays the result.

## How to Run

### Web Calculator
1. Open `Calculator.html` in any modern web browser.
2. Use the buttons to perform calculations.

### Desktop Calculator
1. Ensure Python is installed on your system.
2. Run the script using the command:
   ```bash
   python3 Calculator_2.py