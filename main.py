import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QLineEdit
from backend import Chatbot


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Main Window
        self.setMinimumSize(700, 500)
        self.setWindowTitle("Chatbot app")

        # Add chat area widget
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 480, 320)
        self.chat_area.setReadOnly(True)

        # Add the input field widget
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 340, 480, 40)

        # Add the button
        self.button = QPushButton("Send", self)
        self.button.setGeometry(500, 340, 100, 40)
        self.button.clicked.connect(self.send_message)

        self.show()

    def send_message(self):
        user_input = self.input_field.text().strip()
        self.chat_area.append(f"Me: {user_input}")
        self.input_field.clear()

        chatbot = Chatbot()


app = QApplication(sys.argv)
main_window = ChatbotWindow()
sys.exit(app.exec())
