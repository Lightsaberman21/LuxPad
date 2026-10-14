import board
import json
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import KeysScanner

keyboard = KMKKeyboard()

keyboard.matrix = KeysScanner(
    pins=(board.D8, board.D9, board.D10, board.D11),
    value_when_pressed=False,
)

try:
    with open('keymap.json', 'r') as f:
        config = json.load(f)
        mapped_keys = [getattr(KC, k, KC.NO) for k in config.get('keys', [])]
        keyboard.keymap = [mapped_keys]
except Exception as e:
    print("Error loading keymap.json, defaulting layout:", e)
    keyboard.keymap = [[KC.A, KC.B, KC.C, KC.D]]

if __name__ == '__main__':
    keyboard.go()
