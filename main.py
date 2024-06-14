import tkinter as tk
import keyboard
from functools import partial

class KeyboardApp:
    def __init__(self, root):
        self.root = root
        root.title("Virtual Keyboard")

        # Set background color of the main window
        root.configure(bg="lightblue")

        self.key_widgets = {}
        self.pressed_keys = set()

        self._create_menu()

        # Set background color of the keyboard frame
        self.keyboard_frame = tk.Frame(root, bg="lightblue")
        self.keyboard_frame.pack(padx=10, pady=10)

        self.create_reset_button()
        self.create_exit_button()

        # Bind events to keyboard
        keyboard.on_press(self.on_key_event)
        keyboard.on_release(self.on_key_release)

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
                height=2,
                width=keydata['width'],
                bg="white",
                font=("Helvetica", 10),
                relief="solid",
                bd=1,
                command=partial(self.on_click_event, keydata['key'].lower())
            )
            lbl.grid(row=keydata['row'], column=keydata['col'], columnspan=keydata['width'])
            self.key_widgets[keydata['key'].lower()] = lbl

    def create_reset_button(self):
        reset_button = tk.Button(self.root, text="Reset", command=self.reset_keys, bg="lawngreen")
        reset_button.pack(pady=10)

    def create_exit_button(self):
        exit_button = tk.Button(self.root, text="Exit", command=self.exit_program, bg="lawngreen")
        exit_button.pack(pady=10)

    def exit_program(self):
        self.root.quit()

    def reset_keys(self):
        for key, widget in self.key_widgets.items():
            widget.config(bg="white")
        self.pressed_keys.clear()

    def get_key_str(self, event):
        special_keys = {
            'shift': 'shift',
            'ctrl': 'ctrl',
            'alt': 'alt',
            'backspace': 'backspace',
            'caps lock': 'caps lock',
            'enter': 'enter',
            'space': 'space',
            'esc': 'esc',
            'tab': 'tab',
            'win': 'win',
            '-': '-',
            '=': '=',
            '[': '[',
            ']': ']',
            '/': '/',
            '\\': '\\',
            ';': ';',
            "'": "'",
            ',': ',',
            '.': '.',
            'f11': 'f11',
            'f12': 'f12',
            'up': '↑',
            'down': '↓',
            'right': '→',
            'left': '←',
            '`': '`'
        }
        return special_keys.get(event.name.lower(), str(event.name).lower())

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
                {'key': 'Esc', 'row': 0, 'col': 0, 'width': 2},
                {'key': '1', 'row': 0, 'col': 2, 'width': 2},
                {'key': '2', 'row': 0, 'col': 4, 'width': 2},
                {'key': '3', 'row': 0, 'col': 6, 'width': 2},
                {'key': '4', 'row': 0, 'col': 8, 'width': 2},
                {'key': '5', 'row': 0, 'col': 10, 'width': 2},
                {'key': '6', 'row': 0, 'col': 12, 'width': 2},
                {'key': '7', 'row': 0, 'col': 14, 'width': 2},
                {'key': '8', 'row': 0, 'col': 16, 'width': 2},
                {'key': '9', 'row': 0, 'col': 18, 'width': 2},
                {'key': '0', 'row': 0, 'col': 20, 'width': 2},
                {'key': '-', 'row': 0, 'col': 22, 'width': 2},
                {'key': '=', 'row': 0, 'col': 24, 'width': 2},
                {'key': 'Backspace', 'row': 0, 'col': 26, 'width': 4},
                {'key': 'Tab', 'row': 1, 'col': 0, 'width': 3},
                {'key': 'Q', 'row': 1, 'col': 3, 'width': 2},
                {'key': 'W', 'row': 1, 'col': 5, 'width': 2},
                {'key': 'E', 'row': 1, 'col': 7, 'width': 2},
                {'key': 'R', 'row': 1, 'col': 9, 'width': 2},
                {'key': 'T', 'row': 1, 'col': 11, 'width': 2},
                {'key': 'Y', 'row': 1, 'col': 13, 'width': 2},
                {'key': 'U', 'row': 1, 'col': 15, 'width': 2},
                {'key': 'I', 'row': 1, 'col': 17, 'width': 2},
                {'key': 'O', 'row': 1, 'col': 19, 'width': 2},
                {'key': 'P', 'row': 1, 'col': 21, 'width': 2},
                {'key': '[', 'row': 1, 'col': 23, 'width': 2},
                {'key': ']', 'row': 1, 'col': 25, 'width': 2},
                {'key': '\\', 'row': 1, 'col': 27, 'width': 3},
                {'key': 'Caps Lock', 'row': 2, 'col': 0, 'width': 4},
                {'key': 'A', 'row': 2, 'col': 4, 'width': 2},
                {'key': 'S', 'row': 2, 'col': 6, 'width': 2},
                {'key': 'D', 'row': 2, 'col': 8, 'width': 2},
                {'key': 'F', 'row': 2, 'col': 10, 'width': 2},
                {'key': 'G', 'row': 2, 'col': 12, 'width': 2},
                {'key': 'H', 'row': 2, 'col': 14, 'width': 2},
                {'key': 'J', 'row': 2, 'col': 16, 'width': 2},
                {'key': 'K', 'row': 2, 'col': 18, 'width': 2},
                {'key': 'L', 'row': 2, 'col': 20, 'width': 2},
                {'key': ';', 'row': 2, 'col': 22, 'width': 2},
                {'key': "'", 'row': 2, 'col': 24, 'width': 2},
                {'key': 'Enter', 'row': 2, 'col': 26, 'width': 5},
                {'key': 'Shift', 'row': 3, 'col': 0, 'width': 5},
                {'key': 'Z', 'row': 3, 'col': 5, 'width': 2},
                {'key': 'X', 'row': 3, 'col': 7, 'width': 2},
                {'key': 'C', 'row': 3, 'col': 9, 'width': 2},
                {'key': 'V', 'row': 3, 'col': 11, 'width': 2},
                {'key': 'B', 'row': 3, 'col': 13, 'width': 2},
                {'key': 'N', 'row': 3, 'col': 15, 'width': 2},
                {'key': 'M', 'row': 3, 'col': 17, 'width': 2},
                {'key': ',', 'row': 3, 'col': 19, 'width': 2},
                {'key': '.', 'row': 3, 'col': 21, 'width': 2},
                {'key': '/', 'row': 3, 'col': 23, 'width': 2},
                {'key': 'RShift', 'row': 3, 'col': 25, 'width': 6},
                {'key': 'Ctrl', 'row': 4, 'col': 0, 'width': 3},
                {'key': 'Win', 'row': 4, 'col': 3, 'width': 3},
                {'key': 'Alt', 'row': 4, 'col': 6, 'width': 3},
                {'key': 'Space', 'row': 4, 'col': 9, 'width': 13},
                {'key': 'RAlt', 'row': 4, 'col': 22, 'width': 2},
                {'key': 'Fn', 'row': 4, 'col': 24, 'width': 2},
                {'key': 'RCtrl', 'row': 4, 'col': 26, 'width': 2},
            ],
            "80": [ {'key': 'Esc', 'row': 0, 'col': 0, 'width': 2},
                {'key': 'F1', 'row': 0, 'col': 2, 'width': 2},

                    {'key': 'F2', 'row': 0, 'col': 4, 'width': 2},
                    {'key': 'F3', 'row': 0, 'col': 6, 'width': 2},
                    {'key': 'F4', 'row': 0, 'col': 8, 'width': 2},
                    {'key': 'F5', 'row': 0, 'col': 10, 'width': 2},
                    {'key': 'F6', 'row': 0, 'col': 12, 'width': 2},
                    {'key': 'F7', 'row': 0, 'col': 14, 'width': 2},
                    {'key': 'F8', 'row': 0, 'col': 16, 'width': 2},
                    {'key': 'F9', 'row': 0, 'col': 18, 'width': 2},
                    {'key': 'F10', 'row': 0, 'col': 20, 'width': 2},
                    {'key': 'F11', 'row': 0, 'col': 22, 'width': 2},
                    {'key': 'F12', 'row': 0, 'col': 24, 'width': 2},
                    {'key': 'PrtSc', 'row': 0, 'col': 26, 'width': 2},
                    {'key': 'ScrLk', 'row': 0, 'col': 28, 'width': 2},
                    {'key': 'Pause', 'row': 0, 'col': 30, 'width': 2},
                    {'key': '`', 'row': 1, 'col': 0, 'width': 2},
                    {'key': '1', 'row': 1, 'col': 2, 'width': 2},
                    {'key': '2', 'row': 1, 'col': 4, 'width': 2},
                    {'key': '3', 'row': 1, 'col': 6, 'width': 2},
                    {'key': '4', 'row': 1, 'col': 8, 'width': 2},
                    {'key': '5', 'row': 1, 'col': 10, 'width': 2},
                    {'key': '6', 'row': 1, 'col': 12, 'width': 2},
                    {'key': '7', 'row': 1, 'col': 14, 'width': 2},
                    {'key': '8', 'row': 1, 'col': 16, 'width': 2},
                    {'key': '9', 'row': 1, 'col': 18, 'width': 2},
                    {'key': '0', 'row': 1, 'col': 20, 'width': 2},
                    {'key': '-', 'row': 1, 'col': 22, 'width': 2},
                    {'key': '=', 'row': 1, 'col': 24, 'width': 2},
                    {'key': 'Backspace', 'row': 1, 'col': 26, 'width': 6},
                    {'key': 'Insert', 'row': 1, 'col': 32, 'width': 2},
                    {'key': 'Home', 'row': 1, 'col': 34, 'width': 2},
                    {'key': 'Page Up', 'row': 1, 'col': 36, 'width': 5},
                    {'key': 'Tab', 'row': 2, 'col': 0, 'width': 3},
                    {'key': 'Q', 'row': 2, 'col': 3, 'width': 2},
                    {'key': 'W', 'row': 2, 'col': 5, 'width': 2},
                    {'key': 'E', 'row': 2, 'col': 7, 'width': 2},
                    {'key': 'R', 'row': 2, 'col': 9, 'width': 2},
                    {'key': 'T', 'row': 2, 'col': 11, 'width': 2},
                    {'key': 'Y', 'row': 2, 'col': 13, 'width': 2},
                    {'key': 'U', 'row': 2, 'col': 15, 'width': 2},
                    {'key': 'I', 'row': 2, 'col': 17, 'width': 2},
                    {'key': 'O', 'row': 2, 'col': 19, 'width': 2},
                    {'key': 'P', 'row': 2, 'col': 21, 'width': 2},
                    {'key': '[', 'row': 2, 'col': 23, 'width': 2},
                    {'key': ']', 'row': 2, 'col': 25, 'width': 2},
                    {'key': '\\', 'row': 2, 'col': 27, 'width': 2},
                    {'key': 'Del', 'row': 2, 'col': 29, 'width': 2},
                    {'key': 'End', 'row': 2, 'col': 31, 'width': 2},
                    {'key': 'Page Down', 'row': 2, 'col': 33, 'width': 5},
                    {'key': 'Caps Lock', 'row': 3, 'col': 0, 'width': 4},
                    {'key': 'A', 'row': 3, 'col': 4, 'width': 2},
                    {'key': 'S', 'row': 3, 'col': 6, 'width': 2},
                    {'key': 'D', 'row': 3, 'col': 8, 'width': 2},
                    {'key': 'F', 'row': 3, 'col': 10, 'width': 2},
                    {'key': 'G', 'row': 3, 'col': 12, 'width': 2},
                    {'key': 'H', 'row': 3, 'col': 14, 'width': 2},
                    {'key': 'J', 'row': 3, 'col': 16, 'width': 2},
                    {'key': 'K', 'row': 3, 'col': 18, 'width': 2},
                    {'key': 'L', 'row': 3, 'col': 20, 'width': 2},
                    {'key': ';', 'row': 3, 'col': 22, 'width': 2},
                    {'key': "'", 'row': 3, 'col': 24, 'width': 2},
                    {'key': 'Enter', 'row': 3, 'col': 26, 'width': 6},
                    {'key': 'Shift', 'row': 4, 'col': 0, 'width': 5},
                    {'key': 'Z', 'row': 4, 'col': 5, 'width': 2},
                    {'key': 'X', 'row': 4, 'col': 7, 'width': 2},

                {'key': 'C', 'row': 4, 'col': 9, 'width': 2},
                {'key': 'V', 'row': 4, 'col': 11, 'width': 2},
                {'key': 'B', 'row': 4, 'col': 13, 'width': 2},
                {'key': 'N', 'row': 4, 'col': 15, 'width': 2},
                {'key': 'M', 'row': 4, 'col': 17, 'width': 2},
                {'key': ',', 'row': 4, 'col': 19, 'width': 2},
                {'key': '.', 'row': 4, 'col': 21, 'width': 2},
                {'key': '/', 'row': 4, 'col': 23, 'width': 2},
                {'key': 'RShift', 'row': 4, 'col': 25, 'width': 5},
                {'key': '↑', 'row': 4, 'col': 30, 'width': 2},
                {'key': 'Ctrl', 'row': 5, 'col': 0, 'width': 3},
                {'key': 'Win', 'row': 5, 'col': 3, 'width': 3},
                {'key': 'Alt', 'row': 5, 'col': 6, 'width': 3},
                {'key': 'Space', 'row': 5, 'col': 9, 'width': 13},
                {'key': 'RAlt', 'row': 5, 'col': 22, 'width': 2},
                {'key': 'Fn', 'row': 5, 'col': 24, 'width': 2},
                {'key': 'RCtrl', 'row': 5, 'col': 26, 'width': 2},
                {'key': '←', 'row': 5, 'col': 28, 'width': 2},
                {'key': '↓', 'row': 5, 'col': 30, 'width': 2},
                {'key': '→', 'row': 5, 'col': 32, 'width': 2},],
            "100": [{'key': 'Esc', 'row': 0, 'col': 0, 'width': 2},
                {'key': 'F1', 'row': 0, 'col': 2, 'width': 2},
                {'key': 'F2', 'row': 0, 'col': 4, 'width': 2},
                {'key': 'F3', 'row': 0, 'col': 6, 'width': 2},
                {'key': 'F4', 'row': 0, 'col': 8, 'width': 2},
                {'key': 'F5', 'row': 0, 'col': 10, 'width': 2},
                {'key': 'F6', 'row': 0, 'col': 12, 'width': 2},
                {'key': 'F7', 'row': 0, 'col': 14, 'width': 2},
                {'key': 'F8', 'row': 0, 'col': 16, 'width': 2},
                {'key': 'F9', 'row': 0, 'col': 18, 'width': 2},
                {'key': 'F10', 'row': 0, 'col': 20, 'width': 2},
                {'key': 'F11', 'row': 0, 'col': 22, 'width': 2},
                {'key': 'F12', 'row': 0, 'col': 24, 'width': 2},
                {'key': 'PrtSc', 'row': 0, 'col': 26, 'width': 2},
                {'key': 'ScrLk', 'row': 0, 'col': 28, 'width': 2},
                {'key': 'Pause', 'row': 0, 'col': 30, 'width': 2},

                {'key': '`', 'row': 1, 'col': 0, 'width': 2},
                {'key': '1', 'row': 1, 'col': 2, 'width': 2},
                {'key': '2', 'row': 1, 'col': 4, 'width': 2},
                {'key': '3', 'row': 1, 'col': 6, 'width': 2},
                {'key': '4', 'row': 1, 'col': 8, 'width': 2},
                {'key': '5', 'row': 1, 'col': 10, 'width': 2},
                {'key': '6', 'row': 1, 'col': 12, 'width': 2},
                {'key': '7', 'row': 1, 'col': 14, 'width': 2},
                {'key': '8', 'row': 1, 'col': 16, 'width': 2},
                {'key': '9', 'row': 1, 'col': 18, 'width': 2},
                {'key': '0', 'row': 1, 'col': 20, 'width': 2},
                {'key': '-', 'row': 1, 'col': 22, 'width': 2},
                {'key': '=', 'row': 1, 'col': 24, 'width': 2},
                {'key': 'Backspace', 'row': 1, 'col': 26, 'width': 6},
                {'key': 'Insert', 'row': 1, 'col': 32, 'width': 2},
                {'key': 'Home', 'row': 1, 'col': 34, 'width': 2},
                {'key': 'PgUp', 'row': 1, 'col': 36, 'width': 2},

                {'key': 'Tab', 'row': 2, 'col': 0, 'width': 3},
                {'key': 'Q', 'row': 2, 'col': 3, 'width': 2},
                {'key': 'W', 'row': 2, 'col': 5, 'width': 2},
                {'key': 'E', 'row': 2, 'col': 7, 'width': 2},
                {'key': 'R', 'row': 2, 'col': 9, 'width': 2},
                {'key': 'T', 'row': 2, 'col': 11, 'width': 2},
                {'key': 'Y', 'row': 2, 'col': 13, 'width': 2},
                {'key': 'U', 'row': 2, 'col': 15, 'width': 2},
                {'key': 'I', 'row': 2, 'col': 17, 'width': 2},
                {'key': 'O', 'row': 2, 'col': 19, 'width': 2},
                {'key': 'P', 'row': 2, 'col': 21, 'width': 2},
                {'key': '[', 'row': 2, 'col': 23, 'width': 2},
                {'key': ']', 'row': 2, 'col': 25, 'width': 2},
                {'key': '\\', 'row': 2, 'col': 27, 'width': 2},
                {'key': 'Del', 'row': 2, 'col': 29, 'width': 2},
                {'key': 'End', 'row': 2, 'col': 31, 'width': 2},
                {'key': 'PgDn', 'row': 2, 'col': 33, 'width': 2},

                {'key': 'Caps Lock', 'row': 3, 'col': 0, 'width': 4},
                {'key': 'A', 'row': 3, 'col': 4, 'width': 2},
                {'key': 'S', 'row': 3, 'col': 6, 'width': 2},
                {'key': 'D', 'row': 3, 'col': 8, 'width': 2},
                {'key': 'F', 'row': 3, 'col': 10, 'width': 2},
                {'key': 'G', 'row': 3, 'col': 12, 'width': 2},
                {'key': 'H', 'row': 3, 'col': 14, 'width': 2},
                {'key': 'J', 'row': 3, 'col': 16, 'width': 2},
                {'key': 'K', 'row': 3, 'col': 18, 'width': 2},
                {'key': 'L', 'row': 3, 'col': 20, 'width': 2},
                {'key': ';', 'row': 3, 'col': 22, 'width': 2},
                {'key': "'", 'row': 3, 'col': 24, 'width': 2},
                {'key': 'Enter', 'row': 3, 'col': 26, 'width': 7},
                {'key': 'Shift', 'row': 4, 'col': 0, 'width': 5},
                {'key': 'Z', 'row': 4, 'col': 5, 'width': 2},
                {'key': 'X', 'row': 4, 'col': 7, 'width': 2},
                {'key': 'C', 'row': 4, 'col': 9, 'width': 2},
                {'key': 'V', 'row': 4, 'col': 11, 'width': 2},
                {'key': 'B', 'row': 4, 'col': 13, 'width': 2},
                {'key': 'N', 'row': 4, 'col': 15, 'width': 2},
                {'key': 'M', 'row': 4, 'col': 17, 'width': 2},
                {'key': ',', 'row': 4, 'col': 19, 'width': 2},
                {'key': '.', 'row': 4, 'col': 21, 'width': 2},
                {'key': '/', 'row': 4, 'col': 23, 'width': 2},
                {'key': 'Shift', 'row': 4, 'col': 25, 'width': 9},
                {'key': 'Arrow Up', 'row': 4, 'col': 34, 'width': 2},

                {'key': 'Ctrl', 'row': 5, 'col': 0, 'width': 3},
                {'key': 'Win', 'row': 5, 'col': 3, 'width': 3},
                {'key': 'Alt', 'row': 5, 'col': 6, 'width': 3},
                {'key': 'Space', 'row': 5, 'col': 9, 'width': 12},
                {'key': 'Alt', 'row': 5, 'col': 21, 'width': 3},
                {'key': 'Win', 'row': 5, 'col': 24, 'width': 3},
                {'key': 'Menu', 'row': 5, 'col': 27, 'width': 3},
                {'key': 'Ctrl', 'row': 5, 'col': 30, 'width': 3},
                {'key': 'Arrow Left', 'row': 5, 'col': 33, 'width': 2},
                {'key': 'Arrow Down', 'row': 5, 'col': 35, 'width': 2},
                {'key': 'Arrow Right', 'row': 5, 'col': 37, 'width': 2},

                {'key': 'Num Lock', 'row': 1, 'col': 40, 'width': 2},
                {'key': '/', 'row': 1, 'col': 42, 'width': 2},
                {'key': '*', 'row': 1, 'col': 44, 'width': 2},
                {'key': '-', 'row': 1, 'col': 46, 'width': 2},

                {'key': '7', 'row': 2, 'col': 40, 'width': 2},
                {'key': '8', 'row': 2, 'col': 42, 'width': 2},
                {'key': '9', 'row': 2, 'col': 44, 'width': 2},
                {'key': '+', 'row': 2, 'col': 46, 'width': 2, 'height': 3},

                {'key': '4', 'row': 3, 'col': 40, 'width': 2},
                {'key': '5', 'row': 3, 'col': 42, 'width': 2},
                {'key': '6', 'row': 3, 'col': 44, 'width': 2},

                {'key': '1', 'row': 4, 'col': 40, 'width': 2},
                {'key': '2', 'row': 4, 'col': 42, 'width': 2},
                {'key': '3', 'row': 4, 'col': 44, 'width': 2},
                {'key': 'Enter', 'row': 4, 'col': 46, 'width': 2, 'height': 3},

                {'key': '0', 'row': 5, 'col': 40, 'width': 4},
                {'key': '.', 'row': 5, 'col': 44, 'width': 2},]
        }
        return layouts[layout_percentage]


if __name__ == "__main__":
    root = tk.Tk()
    app = KeyboardApp(root)
    root.mainloop()
