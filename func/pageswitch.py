import keyboard
import os
from config import pages
page = 1
def next(_):
    os.system('cls' if os.name == 'nt' else 'clear')
    global page
    page += 1
    if page in pages:
        pages[page]()
    else:
        return

def back(_):
    global page
    if page == 1:
        return
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        page -= 1
        if page in pages:
            pages[page]()
        else:
            return

def keypressing():
    keyboard.on_press_key("n", next, suppress=False)
    keyboard.on_press_key("b", back, suppress=False)