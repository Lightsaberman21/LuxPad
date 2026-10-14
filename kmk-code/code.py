import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import KeysScanner

keyboard = KMKKeyboard()

keyboard.matrix = KeysScanner(
    pins=(board.D8, board.D9, board.D10, board.D11),
    value_when_pressed=False, 
)

keyboard.keymap = [
    [KC.A, KC.B, KC.C, KC.D]
]

if __name__ == '__main__':
    keyboard.go()