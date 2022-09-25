import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import KeyCode
from pynput import keyboard

TOGGLE_KEY = KeyCode(char=";")
print('Press ; to start/stop')

clicking = False
mouse = Controller()

def clicker():
    while True:
        if clicking:
            mouse.click(Button.left, 1)
            time.sleep(0.001)
        else: time.sleep(0.1)

def toggle_event(key):
    if key == TOGGLE_KEY:
        global clicking
        clicking = not clicking

click_thread = threading.Thread(target=clicker)
click_thread.start()

with keyboard.Listener(on_press=toggle_event) as listener:
    listener.join()