import keyboard
import os
from config import state
from config import pages
from func.filelaunch import option1
from func.filelaunch import option2
from func.filelaunch import option3
from func.filelaunch import option4
from func.filelaunch import option5
from func.filelaunch import option6


def next(_):
    if state.page == 3:
        return
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        state.page += 1
        if state.page in pages:
            pages[state.page]()
        else:
            return

def back(_):
    if state.page == 1:
        return
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        state.page -= 1
        if state.page in pages:
            pages[state.page]()
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