import keyboard
import os
from config import pages
from config import page
from func.filelaunch import option1
from func.filelaunch import option2
from func.filelaunch import option3
from func.filelaunch import option4
from func.filelaunch import option5
from func.filelaunch import option6


def next(_):
    global page
    if page == 2:
        return
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
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
    keyboard.on_press_key("1", option1, suppress=False)
    keyboard.on_press_key("2", option2, suppress=False)
    keyboard.on_press_key("3", option3, suppress=False)
    keyboard.on_press_key("4", option4, suppress=False)
    keyboard.on_press_key("5", option5, suppress=False)
    keyboard.on_press_key("6", option6, suppress=False)