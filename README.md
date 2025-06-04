# Secure Password Generator

This is a simple yet effective password generator application built with Python and PyQt6. It allows users to generate strong, customizable passwords with options to include letters (uppercase and lowercase), numbers, and symbols.

## Features

-   Generate passwords of specified length.
-   Customize character types (letters, numbers, symbols).
-   One-click copy to clipboard functionality.
-   Non-intrusive notification for copied passwords.
-   User-friendly graphical interface.

## Requirements

To run this application, you need Python 3.x and PyQt6. You can install PyQt6 using pip:

```bash
pip install PyQt6
```

## How to Run

1.  **Clone the repository (or download the files):**

    ```bash
    git clone https://github.com/YOUR_GITHUB_USERNAME/secure-password-generator.git
    cd secure-password-generator
    ```

    (Replace `YOUR_GITHUB_USERNAME` with your actual GitHub username and `secure-password-generator` with your repository name)

2.  **Install dependencies:**

    It's recommended to use a virtual environment:

    ```bash
    python -m venv venv
    .venv\Scripts\activate   # On Windows
    # source venv/bin/activate # On macOS/Linux
    
    pip install -r requirements.txt
    ```

3.  **Run the application:**

    ```bash
    python password_generator.py
    # Or on Windows, if `python` is not in PATH:
    # py password_generator.py
    ```

## Usage

1.  **Enter Desired Length:** Type the desired length of your password in the input field. (Default is 12).
2.  **Select Character Types:** Check or uncheck the boxes to include/exclude letters, numbers, and symbols.
3.  **Generate Password:** Click the "Generate Password" button. The generated password will appear in the text area below.
4.  **Copy to Clipboard:** Click the "Copy to Clipboard" button to instantly copy the generated password. A small notification will appear confirming the copy.

## Contributing

Feel free to fork this repository, open issues, or submit pull requests. Any contributions are welcome!

## License

This project is open source and available under the [MIT License](LICENSE). (You might want to create a LICENSE file later)

---

## Developed by

[Your Name/GitHub Username] 