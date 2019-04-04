pip install pynput
from pynput.keyboard import Key, Controller
keyboard = Controller()
keyboard.press(Key.esc)
keyboard.release(Key.esc)
