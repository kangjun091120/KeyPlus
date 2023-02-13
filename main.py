from pynput import mouse, keyboard
import monitor as on
import gui

listener = mouse.Listener(on_move=on.move, on_click=on.click, on_scroll=on.scroll)
listener.start()

with keyboard.Listener(on_press=on.press, on_release=on.release) as listener:
    listener.join()

print("a")
