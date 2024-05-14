import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout
from PyQt6.QtCore import Qt
import keyboard
import pyperclip

class Keyboard(QWidget):
    def init(self):
        super().init()

        self.setWindowTitle('Keyboard')
        self.setGeometry(100, 100, 800, 300)

        # Установка флага, чтобы окно оставалось поверх других окон
        self.setWindowFlags(self.windowFlags() | Qt.WindowType.WindowStaysOnTopHint)

        self.initUI()

    def initUI(self):
        layout = QGridLayout()
        self.setLayout(layout)

        self.buttons = {}

        # Добавляем коды клавиш для английской раскладки
        keys = [
            ("`", 96), ("1", 49), ("2", 50), ("3", 51), ("4", 52), ("5", 53), ("6", 54), ("7", 55), ("8", 56), ("9", 57), ("0", 48),
            ("-", 45), ("=", 61), ("tab", 16777217), ("q", 81), ("w", 87), ("e", 69), ("r", 82), ("t", 84), ("y", 89), ("u", 85),
            ("i", 73), ("o", 79), ("p", 80), ("[", 91), ("]", 93), ("\\", 92), ("caps lock", 16777252), ("a", 65), ("s", 83),
            ("d", 68), ("f", 70), ("g", 71), ("h", 72), ("j", 74), ("k", 75), ("l", 76), (";", 59), ("'", 39), ("shift", 16777248),
            ("z", 90), ("x", 88), ("c", 67), ("v", 86), ("b", 66), ("n", 78), ("m", 77), (",", 44), (".", 46), ("/", 47), ("shift", 16777248),
            ("ctrl", 16777249), ("win", 16777250), ("alt", 16777251), ("space", 32), ("alt", 16777251), ("win", 16777250), ("menu", 16777253),
            ("ctrl", 16777249), ("left", 16777234), ("down", 16777235), ("right", 16777236)
        ]

        # Добавляем коды клавиш для русской раскладки
        russian_keys = [
            ("ё", 96), ("!", 49), ('"', 50), ("№", 51), (";", 52), ("%", 53), (":", 54), ("?", 55), ("*", 56), ("(", 57), (")", 48), ("_", 45), ("+", 61),
            ("tab", 16777217), ("й", 81), ("ц", 87), ("у", 69), ("к", 82), ("е", 84), ("н", 89), ("г", 85), ("ш", 73), ("щ", 79), ("з", 80), ("х", 91), ("ъ", 93), ("/", 92),
            ("caps lock", 16777252), ("ф", 65), ("ы", 83), ("в", 68), ("а", 70), ("п", 71), ("р", 72), ("о", 74), ("л", 75), ("д", 76), ("ж", 59), ("э", 39),
            ("shift", 16777248), ("я", 90), ("ч", 88), ("с", 67), ("м", 86), ("и", 66), ("т", 78), ("ь", 77), ("б", 44), ("ю", 46), (".", 47), ("shift", 16777248),
            ("ctrl", 16777249), ("win", 16777250), ("alt", 16777251), ("space", 32), ("alt", 16777251), ("win", 16777250), ("menu", 16777253),
            ("ctrl", 16777249), ("left", 16777234), ("down", 16777235), ("right", 16777236)
        ]

        row = 0
        col = 0

        for key, key_ru in zip(keys, russian_keys):
            button = QPushButton(key + '\n' + key_ru, self)
            button.setFixedSize(60, 60)
            layout.addWidget(button, row, col)
            self.buttons[key] = button

            col += 1
            if col > 12:
                col = 0
                row += 1

        self.setStyleSheet("QPushButton { font-size: 12px; border: 1px solid black; }")

        # Установка обработчика нажатий клавиш
        keyboard.on_press(self.handle_key_press)

    def handle_key_press(self, event):
        key = event.name
        if key in self.buttons:
            button = self.buttons[key]
            button.setStyleSheet("background-color: green")

    # Переопределение метода closeEvent для предотвращения закрытия окна
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