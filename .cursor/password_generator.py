import random
import string
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
    QLabel, QLineEdit, QPushButton, QCheckBox, QTextEdit, QMessageBox, QGroupBox, 
    QGridLayout)
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QFont

def generate_password(length=12, include_letters=True, include_numbers=True, include_symbols=True):
    """
    Generates a random password of a given length, including specified character types.

    Args:
        length (int): The desired length of the password. Defaults to 12.
        include_letters (bool): Whether to include letters (uppercase and lowercase). Defaults to True.
        include_numbers (bool): Whether to include numbers. Defaults to True.
        include_symbols (bool): Whether to include symbols. Defaults to True.

    Returns:
        str: The generated password.
        None: If no character types are selected.
    """
    characters = ''
    if include_letters:
        characters += string.ascii_letters  # a-z, A-Z
    if include_numbers:
        characters += string.digits  # 0-9
    if include_symbols:
        characters += string.punctuation  # !@#$%^&*()...

    if not characters:
        return None

    password = ''.join(random.choice(characters) for i in range(length))
    return password

class NotificationWidget(QWidget):
    def __init__(self, message, parent=None):
        super().__init__(parent, Qt.WindowType.ToolTip | Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.FramelessWindowHint | Qt.WindowType.Tool)

        layout = QVBoxLayout(self)
        self.label = QLabel(message)
        self.label.setStyleSheet("color: white; background-color: rgba(0, 0, 0, 180); padding: 10px; border-radius: 5px;")
        self.label.setFont(QFont("Arial", 10))
        layout.addWidget(self.label)
        self.setLayout(layout)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.hide_notification)

    def show_notification(self, duration_ms=2000):
        # Position the notification in the bottom right corner of the screen
        screen = QApplication.primaryScreen()
        screen_geometry = screen.geometry()
        
        self.adjustSize()
        notification_width = self.width()
        notification_height = self.height()

        x = screen_geometry.width() - notification_width - 20 # 20px padding from right
        y = screen_geometry.height() - notification_height - 20 # 20px padding from bottom
        self.move(x, y)

        self.show()
        self.timer.start(duration_ms)

    def hide_notification(self):
        self.timer.stop()
        self.close()

class PasswordGeneratorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Secure Password Generator")
        self.setGeometry(100, 100, 480, 420) # Adjusted size
        self.setMinimumSize(480, 420)

        main_layout = QVBoxLayout()
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(20, 20, 20, 20)
        
        # Length input
        length_layout = QHBoxLayout()
        length_label = QLabel("Password Length:")
        length_label.setFont(QFont("Arial", 10))
        self.length_input = QLineEdit("12") # Default value
        self.length_input.setFixedWidth(60)
        self.length_input.setFont(QFont("Arial", 10))
        length_layout.addWidget(length_label)
        length_layout.addWidget(self.length_input)
        length_layout.addStretch(1)
        main_layout.addLayout(length_layout)

        # Character type checkboxes group
        char_type_group = QGroupBox("Character Types")
        char_type_group.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        char_layout = QVBoxLayout()
        char_layout.setSpacing(8)

        self.letters_checkbox = QCheckBox("Include Letters (a-z, A-Z)")
        self.letters_checkbox.setChecked(True)
        self.letters_checkbox.setFont(QFont("Arial", 10))
        
        self.numbers_checkbox = QCheckBox("Include Numbers (0-9)")
        self.numbers_checkbox.setChecked(True)
        self.numbers_checkbox.setFont(QFont("Arial", 10))

        self.symbols_checkbox = QCheckBox("Include Symbols (!@#$%^&*()_+-=[]{}|;:,.<>/?)")
        self.symbols_checkbox.setChecked(True)
        self.symbols_checkbox.setFont(QFont("Arial", 10))

        char_layout.addWidget(self.letters_checkbox)
        char_layout.addWidget(self.numbers_checkbox)
        char_layout.addWidget(self.symbols_checkbox)
        char_type_group.setLayout(char_layout)
        main_layout.addWidget(char_type_group)

        # Generate button
        generate_button = QPushButton("Generate Password")
        generate_button.clicked.connect(self.generate_and_display_password)
        generate_button.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        generate_button.setStyleSheet("QPushButton { background-color: #4CAF50; color: white; border-radius: 5px; padding: 10px; } QPushButton:hover { background-color: #45a049; }")
        main_layout.addWidget(generate_button)

        # Password display
        password_label = QLabel("Generated Password:")
        password_label.setFont(QFont("Arial", 10))
        main_layout.addWidget(password_label)
        
        self.password_display = QTextEdit()
        self.password_display.setReadOnly(True)
        self.password_display.setFixedHeight(80)
        self.password_display.setFont(QFont("Courier New", 12, QFont.Weight.Bold)) # Monospaced font for password
        self.password_display.setStyleSheet("background-color: #f0f0f0; border: 1px solid #ccc; padding: 5px;")
        main_layout.addWidget(self.password_display)

        # Copy to clipboard button
        copy_button = QPushButton("Copy to Clipboard")
        copy_button.clicked.connect(self.copy_password_to_clipboard)
        copy_button.setFont(QFont("Arial", 10))
        copy_button.setStyleSheet("QPushButton { background-color: #2196F3; color: white; border-radius: 5px; padding: 8px; } QPushButton:hover { background-color: #0b7dda; }")
        main_layout.addWidget(copy_button, alignment=Qt.AlignmentFlag.AlignRight)

        self.setLayout(main_layout)

    def generate_and_display_password(self):
        try:
            length = int(self.length_input.text())
            if length <= 0:
                QMessageBox.critical(self, "Input Error", "Password length must be a positive number.")
                return
            elif length > 1000000: # Practical limit
                QMessageBox.warning(self, "Warning", "Generating an extremely long password (over 1 million characters) may consume significant memory and time. A password of 100 billion characters is not feasible to generate and store in memory on typical systems. Please consider a more practical length.")

            letters = self.letters_checkbox.isChecked()
            numbers = self.numbers_checkbox.isChecked()
            symbols = self.symbols_checkbox.isChecked()

            if not letters and not numbers and not symbols:
                QMessageBox.critical(self, "Input Error", "At least one character type (letters, numbers, or symbols) must be selected.")
                return

            password = generate_password(length, letters, numbers, symbols)
            self.password_display.setText(password)

        except ValueError:
            QMessageBox.critical(self, "Input Error", "Invalid input for password length. Please enter an integer.")
        except Exception as e:
            QMessageBox.critical(self, "An error occurred", str(e))

    def copy_password_to_clipboard(self):
        clipboard = QApplication.clipboard()
        password_text = self.password_display.toPlainText()
        if password_text:
            clipboard.setText(password_text)
            notification = NotificationWidget("Password copied to clipboard!")
            notification.show_notification(2000) # Show for 2 seconds
        else:
            QMessageBox.information(self, "Copy Error", "No password to copy!")

if __name__ == "__main__":
    app = QApplication([])
    window = PasswordGeneratorApp()
    window.show()
    app.exec() 