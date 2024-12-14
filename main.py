import keyboard
import os
from func.pages import page_1
from func.pageswitch import keypressing


os.system('cls' if os.name == 'nt' else 'clear')
page_1()
keypressing()
keyboard.wait("q", suppress=True)
