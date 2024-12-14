import os
from config import page
from .pages import title_screen

def option1(_):
    if page == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        title_screen()
        print(" ")
        url = input("Target URL: ")
        if url.startswith("https://"):
            url = "http://" + url[8:]
        file = os.path.join(os.path.dirname(__file__), '..', 'scripts', 'saphyra.py')
        os.system(f"python {file} {url}")
    

def option2(_):
    if page == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        title_screen()
        print(" ")
        url = input("Target URL: ")
        if url.startswith("https://"):
            url = "http://" + url[8:]
        file = os.path.join(os.path.dirname(__file__), '..', 'scripts', 'akira.py')
        os.system(f"python {file} {url}")

def option3(_):
    return

def option4(_):
    return

def option5(_):
    return

def option6(_):
    return




def saphyra(_):
    return

def akira(_):
    return

def Layer7(_):
    return