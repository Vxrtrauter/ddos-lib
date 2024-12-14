import os
import time
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
    if page == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        title_screen()
        print(" ")
        url = input("Target URL: ")
        mode = input("Attack Mode (GET, POST): ")
        if url.startswith("https://"):
            url = "http://" + url[8:]
        if mode == "get" or "GET":
            file = os.path.join(os.path.dirname(__file__), '..', 'scripts', 'layer7.py')
            os.system(f"python {file} -t {mode} {url}")
        if mode == "post" or "POST":
            file = os.path.join(os.path.dirname(__file__), '..', 'scripts', 'layer7.py')
            os.system(f"python {file} -t {mode} {url}")
        else:
            print("Invalid Mode: "+mode)
            option3()
        
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