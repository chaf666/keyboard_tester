import tkinter as tk
from functools import partial


class KeyboardApp:
    def __init__(self, root):
        self.root = root
        root.title("Virtual Keyboard")
class KeyboardApp:
    def __init__(self, root):
        self.root = root
        root.title("Virtual Keyboard")

        # Установка цвета фона основного окна
        root.configure(bg="lightblue")

        self.key_widgets = {}
        self.pressed_keys = set()

        self._create_menu()

        # Установка цвета фона фрейма клавиатуры
        self.keyboard_frame = tk.Frame(root, bg="lightblue")
        self.keyboard_frame.pack(padx=10, pady=10)

        self.create_reset_button()
        self.create_exit_button()

        root.bind("<KeyPress>", self.on_key_event)
        root.bind("<KeyRelease>", self.on_key_release)

    def _create_menu(self):
        menubar = tk.Menu(self.root)
        layout_menu = tk.Menu(menubar, tearoff=0)

        layout_menu.add_command(label="60%", command=partial(self.draw_layout, '60'))
        layout_menu.add_command(label="80%", command=partial(self.draw_layout, '80'))
        layout_menu.add_command(label="100%", command=partial(self.draw_layout, '100'))

        menubar.add_cascade(label="Layout", menu=layout_menu)
        self.root.config(menu=menubar)

    def draw_layout(self, layout_percentage):
        for widget in self.keyboard_frame.winfo_children():
            widget.destroy()
        self.key_widgets = {}
        layout = self.get_layout(layout_percentage)
        for keydata in layout:
            lbl = tk.Button(
                self.keyboard_frame,
                text=keydata['key'],
                height=1,
                width=keydata['width'],
                bg="white",  # Установка цвета фона кнопок клавиатуры
                font=("Helvetica", 16),
                relief="solid",
                bd=1,
                command=partial(self.on_click_event, keydata['key'].lower())
            )
            lbl.grid(row=keydata['row'], column=keydata['col'], columnspan=keydata['width'])
            self.key_widgets[keydata['key'].lower()] = lbl

    def create_reset_button(self):
        # Установка цвета фона кнопки сброса
        reset_button = tk.Button(self.root, text="Reset", command=self.reset_keys, bg="lawngreen")
        reset_button.pack(pady=10)

    def create_exit_button(self):
        # Создание кнопки выхода
        exit_button = tk.Button(self.root, text="Exit", command=self.exit_program, bg="lawngreen")
        exit_button.pack(pady=20)

    def exit_program(self):
        self.root.quit()

    def reset_keys(self):
        for key, widget in self.key_widgets.items():
            widget.config(bg="white")
        self.pressed_keys.clear()

    def get_key_str(self, event):
        special_keys = {
            'Shift_L': 'shift',
            'Shift_R': 'rshift',
            'Control_L': 'ctrl',
            'Control_R': 'rctrl',
            'Alt_L': 'alt',
            'Alt_R': 'ralt',
            'BackSpace': '⌫',
            'Caps_Lock': '🡇',
            'Return': 'enter',
            'space': 'space',
            'Escape': 'esc',
            'Tab': 'tab',
            'Win_L': 'win',
            'Win_R': 'win',
            'minus': '-',
            'equal': '=',
            'bracketleft': '[',
            'bracketright': ']',
            'slash': '/',
            'backslash': '\\',
            'semicolon': ';',
            'apostrophe': "'",
            'comma': ',',
            'period': '.',
            'F11': 'f11',
            'F12': 'f12',
            'Up':  '↑',
            'Down': '↓',
            'Right': '→',
            'Left': '←',
            'grave': '`',
            'Delete': 'del',
            'Scroll_Lock': 'scrlk',
            'Prior': 'pgup',
            'Next': 'pgdn',
            'Print': 'prtsc',
            'Kp_Lock': 'num'
        }

        return special_keys.get(event.keysym, str(event.keysym).lower())

    def on_key_event(self, event):
        key_str = self.get_key_str(event)
        if key_str in self.key_widgets:
            self.key_widgets[key_str].config(bg="lawngreen")
            self.pressed_keys.add(key_str)


    def on_click_event(self, key_str):
        if key_str in self.key_widgets:
            self.key_widgets[key_str].config(bg="lawngreen")

    def on_key_release(self, event):
        key_str = self.get_key_str(event)
        if key_str in self.key_widgets and key_str not in self.pressed_keys:
            self.key_widgets[key_str].config(bg="white")


    def get_layout(self, layout_percentage):
        layouts = {
            "60": [
                {'key': 'Esc', 'row': 0, 'col': 0, 'width': 3},
                {'key': '1', 'row': 0, 'col': 3, 'width': 3},
                {'key': '2', 'row': 0, 'col': 6, 'width': 3},
                {'key': '3', 'row': 0, 'col': 9, 'width': 3},
                {'key': '4', 'row': 0, 'col': 12, 'width': 3},
                {'key': '5', 'row': 0, 'col': 15, 'width': 3},
                {'key': '6', 'row': 0, 'col': 18, 'width': 3},
                {'key': '7', 'row': 0, 'col': 21, 'width': 3},
                {'key': '8', 'row': 0, 'col': 24, 'width': 3},
                {'key': '9', 'row': 0, 'col': 27, 'width': 3},
                {'key': '0', 'row': 0, 'col': 30, 'width': 3},
                {'key': '-', 'row': 0, 'col': 33, 'width': 3},
                {'key': '=', 'row': 0, 'col': 36, 'width': 3},
                {'key': '⌫', 'row': 0, 'col': 39, 'width': 8},
                {'key': 'Home', 'row': 0, 'col': 47, 'width': 4},
                {'key': 'Tab', 'row': 1, 'col': 0, 'width': 4},
                {'key': 'Q', 'row': 1, 'col': 4, 'width': 3},
                {'key': 'W', 'row': 1, 'col': 7, 'width': 3},
                {'key': 'E', 'row': 1, 'col': 10, 'width': 3},
                {'key': 'R', 'row': 1, 'col': 13, 'width': 3},
                {'key': 'T', 'row': 1, 'col': 16, 'width': 3},
                {'key': 'Y', 'row': 1, 'col': 19, 'width': 3},
                {'key': 'U', 'row': 1, 'col': 22, 'width': 3},
                {'key': 'I', 'row': 1, 'col': 25, 'width': 3},
                {'key': 'O', 'row': 1, 'col': 28, 'width': 3},
                {'key': 'P', 'row': 1, 'col': 31, 'width': 3},
                {'key': '[', 'row': 1, 'col': 34, 'width': 3},
                {'key': ']', 'row': 1, 'col': 37, 'width': 3},
                {'key': '\\', 'row': 1, 'col': 40, 'width': 7},
                {'key': 'PgUp', 'row': 1, 'col': 47, 'width': 4},
                {'key': '🡇', 'row': 2, 'col': 0, 'width': 5},
                {'key': 'A', 'row': 2, 'col': 5, 'width': 3},
                {'key': 'S', 'row': 2, 'col': 8, 'width': 3},
                {'key': 'D', 'row': 2, 'col': 11, 'width': 3},
                {'key': 'F', 'row': 2, 'col': 14, 'width': 3},
                {'key': 'G', 'row': 2, 'col': 17, 'width': 3},
                {'key': 'H', 'row': 2, 'col': 20, 'width': 3},
                {'key': 'J', 'row': 2, 'col': 23, 'width': 3},
                {'key': 'K', 'row': 2, 'col': 26, 'width': 3},
                {'key': 'L', 'row': 2, 'col': 29, 'width': 3},
                {'key': ';', 'row': 2, 'col': 32, 'width': 3},
                {'key': "'", 'row': 2, 'col': 35, 'width': 3},
                {'key': 'Enter', 'row': 2, 'col': 38, 'width': 9},
                {'key': 'PgDn', 'row': 2, 'col': 47, 'width': 4},
                {'key': 'Shift', 'row': 3, 'col': 0, 'width': 7},
                {'key': 'Z', 'row': 3, 'col': 7, 'width': 3},
                {'key': 'X', 'row': 3, 'col': 10, 'width': 3},
                {'key': 'C', 'row': 3, 'col': 13, 'width': 3},
                {'key': 'V', 'row': 3, 'col': 16, 'width': 3},
                {'key': 'B', 'row': 3, 'col': 19, 'width': 3},
                {'key': 'N', 'row': 3, 'col': 22, 'width': 3},
                {'key': 'M', 'row': 3, 'col': 25, 'width': 3},
                {'key': ',', 'row': 3, 'col': 28, 'width': 3},
                {'key': '.', 'row': 3, 'col': 31, 'width': 3},
                {'key': '/', 'row': 3, 'col': 34, 'width': 3},
                {'key': 'RShift', 'row': 3, 'col': 37, 'width': 8},
                {'key': '↑', 'row': 3, 'col': 44, 'width': 3},
                {'key': 'End', 'row': 3, 'col': 47, 'width': 4},
                {'key': 'Ctrl', 'row': 4, 'col': 0, 'width': 4},
                {'key': 'Win', 'row': 4, 'col': 4, 'width': 4},
                {'key': 'Alt', 'row': 4, 'col': 8, 'width': 4},
                {'key': 'Space', 'row': 4, 'col': 10, 'width': 23},
                {'key': 'RAlt', 'row': 4, 'col': 31, 'width': 3},
                {'key': 'Fn', 'row': 4, 'col': 34, 'width': 3},
                {'key': 'RCtrl', 'row': 4, 'col': 37, 'width': 4},
                {'key': '←', 'row': 4, 'col': 41, 'width': 3},
                {'key': '↓', 'row': 4, 'col': 44, 'width': 3},
                {'key': '→', 'row': 4, 'col': 47, 'width': 4},
            ],
            "80": [{'key': 'Esc', 'row': 0, 'col': 0, 'width': 3},
                   {'key': 'F1', 'row': 0, 'col': 4, 'width': 3},
                   {'key': 'F2', 'row': 0, 'col': 7, 'width': 3},
                   {'key': 'F3', 'row': 0, 'col': 10, 'width': 3},
                   {'key': 'F4', 'row': 0, 'col': 13, 'width': 3},
                   {'key': 'F5', 'row': 0, 'col': 19, 'width': 3},
                   {'key': 'F6', 'row': 0, 'col': 22, 'width': 3},
                   {'key': 'F7', 'row': 0, 'col': 25, 'width': 3},
                   {'key': 'F8', 'row': 0, 'col': 28, 'width': 3},
                   {'key': 'F9', 'row': 0, 'col': 34, 'width': 3},
                   {'key': 'F10', 'row': 0, 'col': 37, 'width': 3},
                   {'key': 'F11', 'row': 0, 'col': 40, 'width': 3},
                   {'key': 'F12', 'row': 0, 'col': 43, 'width': 3},
                   {'key': 'PrtSc', 'row': 0, 'col': 52, 'width': 5},
                   {'key': 'ScrLk', 'row': 0, 'col': 57, 'width': 5},
                   {'key': 'Pause', 'row': 0, 'col': 62, 'width': 5},
                   {'key': '`', 'row': 1, 'col': 0, 'width': 3},
                   {'key': '1', 'row': 1, 'col': 3, 'width': 3},
                   {'key': '2', 'row': 1, 'col': 6, 'width': 3},
                   {'key': '3', 'row': 1, 'col': 9, 'width': 3},
                   {'key': '4', 'row': 1, 'col': 12, 'width': 3},
                   {'key': '5', 'row': 1, 'col': 15, 'width': 3},
                   {'key': '6', 'row': 1, 'col': 18, 'width': 3},
                   {'key': '7', 'row': 1, 'col': 21, 'width': 3},
                   {'key': '8', 'row': 1, 'col': 24, 'width': 3},
                   {'key': '9', 'row': 1, 'col': 27, 'width': 3},
                   {'key': '0', 'row': 1, 'col': 30, 'width': 3},
                   {'key': '-', 'row': 1, 'col': 33, 'width': 3},
                   {'key': '=', 'row': 1, 'col': 36, 'width': 3},
                   {'key': '⌫', 'row': 1, 'col': 39, 'width': 8},
                   {'key': 'Insert', 'row': 1, 'col': 52, 'width': 5},
                   {'key': 'Home', 'row': 1, 'col': 57, 'width': 5},
                   {'key': 'PgUp', 'row': 1, 'col': 62, 'width': 5},
                   {'key': 'Tab', 'row': 2, 'col': 0, 'width': 4},
                   {'key': 'Q', 'row': 2, 'col': 4, 'width': 3},
                   {'key': 'W', 'row': 2, 'col': 7, 'width': 3},
                   {'key': 'E', 'row': 2, 'col': 10, 'width': 3},
                   {'key': 'R', 'row': 2, 'col': 13, 'width': 3},
                   {'key': 'T', 'row': 2, 'col': 16, 'width': 3},
                   {'key': 'Y', 'row': 2, 'col': 19, 'width': 3},
                   {'key': 'U', 'row': 2, 'col': 22, 'width': 3},
                   {'key': 'I', 'row': 2, 'col': 25, 'width': 3},
                   {'key': 'O', 'row': 2, 'col': 28, 'width': 3},
                   {'key': 'P', 'row': 2, 'col': 31, 'width': 3},
                   {'key': '[', 'row': 2, 'col': 34, 'width': 3},
                   {'key': ']', 'row': 2, 'col': 37, 'width': 3},
                   {'key': '\\', 'row': 2, 'col': 40, 'width': 7},
                   {'key': 'Del', 'row': 2, 'col': 52, 'width': 5},
                   {'key': 'End', 'row': 2, 'col': 57, 'width': 5},
                   {'key': 'PgDn', 'row': 2, 'col': 62, 'width': 5},
                   {'key': '🡇', 'row': 3, 'col': 0, 'width': 5},
                   {'key': 'A', 'row': 3, 'col': 5, 'width': 3},
                   {'key': 'S', 'row': 3, 'col': 8, 'width': 3},
                   {'key': 'D', 'row': 3, 'col': 11, 'width': 3},
                   {'key': 'F', 'row': 3, 'col': 14, 'width': 3},
                   {'key': 'G', 'row': 3, 'col': 17, 'width': 3},
                   {'key': 'H', 'row': 3, 'col': 20, 'width': 3},
                    {'key': 'J', 'row': 3, 'col': 23, 'width': 3},
                    {'key': 'K', 'row': 3, 'col': 26, 'width': 3},
                    {'key': 'L', 'row': 3, 'col': 29, 'width': 3},
                    {'key': ';', 'row': 3, 'col': 32, 'width': 3},
                    {'key': "'", 'row': 3, 'col': 35, 'width': 3},
                    {'key': 'Enter', 'row': 3, 'col': 38, 'width': 9},
                    {'key': 'Shift', 'row': 4, 'col': 0, 'width': 7},
                    {'key': 'Z', 'row': 4, 'col': 7, 'width': 3},
                    {'key': 'X', 'row': 4, 'col': 10, 'width': 3},
                    {'key': 'C', 'row': 4, 'col': 13, 'width': 3},
                    {'key': 'V', 'row': 4, 'col': 16, 'width': 3},
                    {'key': 'B', 'row': 4, 'col': 19, 'width': 3},
                    {'key': 'N', 'row': 4, 'col': 22, 'width': 3},
                    {'key': 'M', 'row': 4, 'col': 25, 'width': 3},
                    {'key': ',', 'row': 4, 'col': 28, 'width': 3},
                    {'key': '.', 'row': 4, 'col': 31, 'width': 3},
                    {'key': '/', 'row': 4, 'col': 34, 'width': 3},
                    {'key': 'RShift', 'row': 4, 'col': 37, 'width': 10},
                    {'key': '↑', 'row': 4, 'col': 57, 'width': 3},
                    {'key': 'Ctrl', 'row': 5, 'col': 0, 'width': 4},
                    {'key': 'Win', 'row': 5, 'col': 4, 'width': 4},
                    {'key': 'Alt', 'row': 5, 'col': 8, 'width': 4},
                    {'key': 'Space', 'row': 5, 'col': 10, 'width': 23},
                    {'key': 'RAlt', 'row': 5, 'col': 31, 'width': 3},
                    {'key': 'Fn', 'row': 5, 'col': 38, 'width': 3},
                    {'key': 'Menu', 'row': 5, 'col': 34, 'width': 4},
                    {'key': 'RCtrl', 'row': 5, 'col': 41, 'width': 5},
                    {'key': '←', 'row': 5, 'col': 54, 'width': 3},
                    {'key': '↓', 'row': 5, 'col': 57, 'width': 3},
                    {'key': '→', 'row': 5, 'col': 60, 'width': 3},],
            "100": [{'key': 'Esc', 'row': 0, 'col': 0, 'width': 3},
                    {'key': 'F1', 'row': 0, 'col': 4, 'width': 3},
                    {'key': 'F2', 'row': 0, 'col': 7, 'width': 3},
                    {'key': 'F3', 'row': 0, 'col': 10, 'width': 3},
                    {'key': 'F4', 'row': 0, 'col': 13, 'width': 3},
                    {'key': 'F5', 'row': 0, 'col': 19, 'width': 3},
                    {'key': 'F6', 'row': 0, 'col': 22, 'width': 3},
                    {'key': 'F7', 'row': 0, 'col': 25, 'width': 3},
                    {'key': 'F8', 'row': 0, 'col': 28, 'width': 3},
                    {'key': 'F9', 'row': 0, 'col': 34, 'width': 3},
                    {'key': 'F10', 'row': 0, 'col': 37, 'width': 3},
                    {'key': 'F11', 'row': 0, 'col': 40, 'width': 3},
                    {'key': 'F12', 'row': 0, 'col': 43, 'width': 3},
                    {'key': 'PrtSc', 'row': 0, 'col': 52, 'width': 5},
                    {'key': 'ScrLk', 'row': 0, 'col': 57, 'width': 5},
                    {'key': 'Pause', 'row': 0, 'col': 62, 'width': 5},
                    {'key': '`', 'row': 1, 'col': 0, 'width': 3},
                    {'key': '1', 'row': 1, 'col': 3, 'width': 3},
                    {'key': '2', 'row': 1, 'col': 6, 'width': 3},
                    {'key': '3', 'row': 1, 'col': 9, 'width': 3},
                    {'key': '4', 'row': 1, 'col': 12, 'width': 3},
                    {'key': '5', 'row': 1, 'col': 15, 'width': 3},
                    {'key': '6', 'row': 1, 'col': 18, 'width': 3},
                    {'key': '7', 'row': 1, 'col': 21, 'width': 3},
                    {'key': '8', 'row': 1, 'col': 24, 'width': 3},
                    {'key': '9', 'row': 1, 'col': 27, 'width': 3},
                    {'key': '0', 'row': 1, 'col': 30, 'width': 3},
                    {'key': '-', 'row': 1, 'col': 33, 'width': 3},
                    {'key': '=', 'row': 1, 'col': 36, 'width': 3},
                    {'key': '⌫', 'row': 1, 'col': 39, 'width': 8},
                    {'key': 'Insert', 'row': 1, 'col': 52, 'width': 5},
                    {'key': 'Home', 'row': 1, 'col': 57, 'width': 5},
                    {'key': 'PgUp', 'row': 1, 'col': 62, 'width': 5},
                    {'key': 'Tab', 'row': 2, 'col': 0, 'width': 4},
                    {'key': 'Q', 'row': 2, 'col': 4, 'width': 3},
                    {'key': 'W', 'row': 2, 'col': 7, 'width': 3},
                    {'key': 'E', 'row': 2, 'col': 10, 'width': 3},
                    {'key': 'R', 'row': 2, 'col': 13, 'width': 3},
                    {'key': 'T', 'row': 2, 'col': 16, 'width': 3},
                    {'key': 'Y', 'row': 2, 'col': 19, 'width': 3},
                    {'key': 'U', 'row': 2, 'col': 22, 'width': 3},
                    {'key': 'I', 'row': 2, 'col': 25, 'width': 3},
                    {'key': 'O', 'row': 2, 'col': 28, 'width': 3},
                    {'key': 'P', 'row': 2, 'col': 31, 'width': 3},
                    {'key': '[', 'row': 2, 'col': 34, 'width': 3},
                    {'key': ']', 'row': 2, 'col': 37, 'width': 3},
                    {'key': '\\', 'row': 2, 'col': 40, 'width': 7},
                    {'key': 'Del', 'row': 2, 'col': 52, 'width': 5},
                    {'key': 'End', 'row': 2, 'col': 57, 'width': 5},
                    {'key': 'PgDn', 'row': 2, 'col': 62, 'width': 5},
                    {'key': '🡇', 'row': 3, 'col': 0, 'width': 5},
                    {'key': 'A', 'row': 3, 'col': 5, 'width': 3},
                    {'key': 'S', 'row': 3, 'col': 8, 'width': 3},
                    {'key': 'D', 'row': 3, 'col': 11, 'width': 3},
                    {'key': 'F', 'row': 3, 'col': 14, 'width': 3},
                    {'key': 'G', 'row': 3, 'col': 17, 'width': 3},
                    {'key': 'H', 'row': 3, 'col': 20, 'width': 3},
                    {'key': 'J', 'row': 3, 'col': 23, 'width': 3},
                    {'key': 'K', 'row': 3, 'col': 26, 'width': 3},
                    {'key': 'L', 'row': 3, 'col': 29, 'width': 3},
                    {'key': ';', 'row': 3, 'col': 32, 'width': 3},
                    {'key': "'", 'row': 3, 'col': 35, 'width': 3},
                    {'key': 'Enter', 'row': 3, 'col': 38, 'width': 9},
                    {'key': 'Shift', 'row': 4, 'col': 0, 'width': 7},
                    {'key': 'Z', 'row': 4, 'col': 7, 'width': 3},
                    {'key': 'X', 'row': 4, 'col': 10, 'width': 3},
                    {'key': 'C', 'row': 4, 'col': 13, 'width': 3},
                    {'key': 'V', 'row': 4, 'col': 16, 'width': 3},
                    {'key': 'B', 'row': 4, 'col': 19, 'width': 3},
                    {'key': 'N', 'row': 4, 'col': 22, 'width': 3},
                    {'key': 'M', 'row': 4, 'col': 25, 'width': 3},
                    {'key': ',', 'row': 4, 'col': 28, 'width': 3},
                    {'key': '.', 'row': 4, 'col': 31, 'width': 3},
                    {'key': '/', 'row': 4, 'col': 34, 'width': 3},
                    {'key': 'RShift', 'row': 4, 'col': 37, 'width': 10},
                    {'key': '↑', 'row': 4, 'col': 57, 'width': 3},
                    {'key': 'Ctrl', 'row': 5, 'col': 0, 'width': 4},
                    {'key': 'Win', 'row': 5, 'col': 4, 'width': 4},
                    {'key': 'Alt', 'row': 5, 'col': 8, 'width': 4},
                    {'key': 'Space', 'row': 5, 'col': 10, 'width': 23},
                    {'key': 'RAlt', 'row': 5, 'col': 31, 'width': 3},
                    {'key': 'Fn', 'row': 5, 'col': 38, 'width': 3},
                    {'key': 'Menu', 'row': 5, 'col': 34, 'width': 4},
                    {'key': 'RCtrl', 'row': 5, 'col': 41, 'width': 5},
                    {'key': '←', 'row': 5, 'col': 54, 'width': 3},
                    {'key': '↓', 'row': 5, 'col': 57, 'width': 3},
                    {'key': '→', 'row': 5, 'col': 60, 'width': 3},
                    {'key': 'Num', 'row': 1, 'col': 72, 'width': 3},
                    {'key': '/', 'row': 1, 'col': 75, 'width': 3},
                    {'key': '*', 'row': 1, 'col': 78, 'width': 3},
                    {'key': '-', 'row': 1, 'col': 81, 'width': 3},
                    {'key': '7', 'row': 2, 'col': 72, 'width': 3},
                    {'key': '8', 'row': 2, 'col': 75, 'width': 3},
                    {'key': '9', 'row': 2, 'col': 78, 'width': 3},
                    {'key': '+', 'row': 2, 'col': 81, 'width': 3, 'height': 2},
                    {'key': '4', 'row': 3, 'col': 72, 'width': 3},
                    {'key': '5', 'row': 3, 'col': 75, 'width': 3},
                    {'key': '6', 'row': 3, 'col': 78, 'width': 3},
                    {'key': '1', 'row': 4, 'col': 72, 'width': 3},
                    {'key': '2', 'row': 4, 'col': 75, 'width': 3},
                    {'key': '3', 'row': 4, 'col': 78, 'width': 3},
                    {'key': 'Enter', 'row': 4, 'col': 81, 'width': 3, 'height': 2},
                    {'key': '0', 'row': 5, 'col': 71, 'width': 7},
                    {'key': '.', 'row': 5, 'col': 78, 'width': 3},]
        }
        return layouts[layout_percentage]


if __name__ == "__main__":
    root = tk.Tk()
    app = KeyboardApp(root)
    root.mainloop()
