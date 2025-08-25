# Strong Password Generator

## Overview
This is a Python application that generates strong, random passwords using a graphical user interface (GUI) built with Tkinter. Users can specify the password length and select character sets (uppercase letters, lowercase letters, digits, and special characters) to include in the generated password.

## Features
- **Customizable Password Length**: Users can input the desired number of characters for the password.
- **Character Set Selection**: Options to include:
  - Uppercase letters (A-Z)
  - Lowercase letters (a-z)
  - Digits (0-9)
  - Special characters (e.g., !@#$%^&*())
- **User-Friendly Interface**: A clean GUI with a light blue theme, buttons for character set selection, and a generate button to create the password.
- **Error Handling**: Displays warnings for invalid inputs (e.g., non-numeric length or no character sets selected).
- **Secure Randomization**: Uses Python's `random` module to generate passwords.

## Requirements
- **Python**: Version 3.x
- **Tkinter**: Included with standard Python installations

## Installation
1. Ensure Python 3.x is installed on your system.
2. No additional libraries are required, as Tkinter is part of Python's standard library.
3. Save the script as `password_generator.py`.

## Usage
1. Run the script:
   ```bash
   python password_generator.py
   ```
2. The GUI will open in a maximized window.
3. Enter the desired password length in the input field.
4. Click the buttons to select which character sets to include (Upper-Case, Lower-Case, Digits, Special Character).
5. Click the "Generate Password" button to create a password.
6. The generated password will be displayed below the buttons.
7. If an error occurs (e.g., invalid length or no character sets selected), an error message will be displayed.

## Code Structure
- **Global Variables**:
  - `all_character`: Stores the combined character set based on user selections.
  - `generate`: Stores the generated password.
- **Functions**:
  - `is_l_letter()`: Adds lowercase letters to the character set.
  - `is_u_letter()`: Adds uppercase letters to the character set.
  - `is_digits()`: Adds digits to the character set.
  - `is_special()`: Adds special characters to the character set.
  - `generate_password()`: Generates the password based on user input and selected character sets.
- **GUI Elements**:
  - Labels, Entry field, Buttons, and Result Label for user interaction and feedback.

## Example
- Input: Length = 12, Select Upper-Case and Digits
- Output: `Generated Password: K7N4P8X2M9Q5`

## Limitations
- The script uses the `random` module, which is not cryptographically secure. For high-security applications, consider using the `secrets` module.
- No option to copy the generated password to the clipboard.
- No password strength indicator.

## Future Improvements
- Replace `random` with `secrets` for cryptographically secure password generation.
- Add a "Copy to Clipboard" button.
- Implement a password strength meter.
- Use Checkbuttons instead of Buttons for character set selection to improve UX.
- Add validation for minimum/maximum password length.

## License
This project is open-source and available under the MIT License.
