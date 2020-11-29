from pynput.keyboard import Key, Controller
import time
time.sleep(5)
Keyboard = Controller()
while True:
      for letter in "Use it to Surprise NOT HARM":
            Keyboard.press(letter)
            Keyboard.release(letter)
      Keyboard.press(Key.enter)
      Keyboard.release(Key.enter)
