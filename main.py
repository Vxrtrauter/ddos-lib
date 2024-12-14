import keyboard
import os
from func.pages import page_1
from func.pageswitch import keypressing
# thanks keksnino for pasting 9 lines of my code into filelaunch.py <3 (jk)

os.system('cls' if os.name == 'nt' else 'clear')
page_1()
keypressing()
keyboard.wait("q", suppress=True)
