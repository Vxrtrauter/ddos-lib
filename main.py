import keyboard
import os
from func.pages import page_1
from func.keyhandler import keypressing
# thanks keksnino for pasting 9 lines <3 (jk)



os.system('cls' if os.name == 'nt' else 'clear')
page_1()
keypressing()
keyboard.wait("q", suppress=True)
