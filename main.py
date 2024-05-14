import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout
from PyQt6.QtCore import Qt
import keyboard


class Keyboard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Keyboard')
        self.setGeometry(100, 100, 800, 300)
        self.setWindowFlags(self.windowFlags() | Qt.WindowType.WindowStaysOnTopHint)
        self.initUI()

    def initUI(self):
        layout = QGridLayout()
        self.setLayout(layout)

        self.buttons = {}

        keys = [
            "`", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "=",
            "tab", "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "[", "]", "\\",
            "caps lock", "a", "s", "d", "f", "g", "h", "j", "k", "l", ";", "'",
            "shift", "z", "x", "c", "v", "b", "n", "m", ",", ".", "/",
            "shift", "ctrl", "win", "alt", "space", "alt", "win", "menu", "ctrl",
            "left", "down", "right"
        ]

        russian_keys = [
            "ё", "!", '"', "№", ";", "%", ":", "?", "*", "(", ")", "_", "+",
            "tab", "й", "ц", "у", "к", "е", "н", "г", "ш", "щ", "з", "х", "ъ", "/",
            "caps lock", "ф", "ы", "в", "а", "п", "р", "о", "л", "д", "ж", "э",
            "shift", "я", "ч", "с", "м", "и", "т", "ь", "б", "ю", ".",
            "shift", "ctrl", "win", "alt", "space", "alt", "win", "menu", "ctrl",
            "left", "down", "right"
        ]
        keys_CAPS = [
            "`", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "=",
            "tab", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "[", "]", "\\",
            "caps lock", "A", "S", "D", "F", "G", "H", "J", "K", "L", ";", "'",
            "shift", "Z", "X", "C", "V", "B", "N", "M", ",", ".", "/",
            "shift", "ctrl", "win", "alt", "space", "alt", "win", "menu", "ctrl",
            "left", "down", "right"
        ]
        russian_keys_CAPS = [
            "ё", "!", '"', "№", ";", "%", ":", "?", "*", "(", ")", "_", "+",
            "tab", "Й", "Ц", "У", "К", "Е", "Н", "Г", "Ш", "Щ", "З", "Х", "Ъ", "/",
            "caps lock", "Ф", "Ы", "В", "А", "П", "Р", "О", "Л", "Д", "Ж", "Э",
            "shift", "Я", "Ч", "С", "М", "И", "Т", "Ь", "Б", "Ю", ".",
            "shift", "ctrl", "win", "alt", "space", "alt", "win", "menu", "ctrl",
            "left", "down", "right"
        ]

        row = 0
        col = 0
        gay = 0
        hui = 0

        for key, key_ru, key_caps, key_caps_ru in zip(keys, russian_keys, keys_CAPS, russian_keys_CAPS):
            button = QPushButton(key_caps + '\n' + key_caps_ru, self)
            button.setText(key + '\n' + key_ru)
            button.setFixedSize(60, 60)
            layout.addWidget(button, row, col)
            self.buttons[key_caps] = button
            self.buttons[key] = button
            col += 1
            if col > 12:
                col = 0
                row += 1


        self.setStyleSheet("QPushButton { font-size: 12px; border: 1px solid black; }")

        keyboard.on_press(self.handle_key_press)

    def handle_key_press(self, event):
        key = event.name
        if key in self.buttons:
            button = self.buttons[key]
            button.setStyleSheet("background-color: green")

            # Проверяем, была ли нажата клавиша Caps Lock
            if keyboard.is_pressed('caps lock'):
                # Если Caps Lock нажат, то преобразуем название клавиши к верхнему регистру
                key = key.upper()

            # Отображаем символы нажатых клавиш в верхнем регистре, если Caps Lock нажат
            button.setText(key)

    def closeEvent(self, event):
        keyboard.unhook_all()
        event.accept()


def main():
    app = QApplication(sys.argv)
    window = Keyboard()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

