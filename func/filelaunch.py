import os
from config import state
from .pages import title_screen
from .pages import page_1

def option1(_):
    if state.page == 1:
        saphyra(_)
    

def option2(_):
    if state.page == 1:
        akira(_)
        

def option3(_):
    if state.page == 1:
        Layer7(_)

def option4(_):
    if state.page == 1:
        blackhorizon(_)

def option5(_):
    return

def option6(_):
    return




def saphyra(_):
    os.system("cls" if os.name == "nt" else "clear")
    title_screen()
    print(" ")
    url = input("Target URL: ")
    if url.startswith("https://"):
        url = "http://" + url[8:]
    file = os.path.join(os.path.dirname(__file__), "..", "scripts", "saphyra.py")
    os.system(f"python {file} {url}")
    os.system("cls" if os.name == "nt" else "clear")
    page_1()

def akira(_):
    os.system("cls" if os.name == "nt" else "clear")
    title_screen()
    print(" ")
    url = input("Target URL: ")
    if url.startswith("https://"):
       url = "http://" + url[8:]
    file = os.path.join(os.path.dirname(__file__), "..", "scripts", "akira.py")
    os.system(f"python {file} {url}")
    os.system("cls" if os.name == "nt" else "clear")
    page_1()

def Layer7(_):
    os.system("cls" if os.name == "nt" else "clear")
    title_screen()
    print(" ")
    url = input("Target URL: ")
    mode = input("Attack Mode (GET, POST): ")
    if url.startswith("https://"):
        url = "http://" + url[8:]
    if mode.lower in ["get", "post"]:
        file = os.path.join(os.path.dirname(__file__), "..", "scripts", "layer7.py")
        os.system(f"python {file} -t {mode} {url}")
        os.system("cls" if os.name == "nt" else "clear")
        page_1()

    else:
        print("Invalid Mode: "+mode)
        option3()
        

def blackhorizon(_):
    os.system("cls" if os.name == "nt" else "clear")
    title_screen()
    print(" ")
    url = input("Target URL: ")
    clouds = input("Concurrent Clouds (default: 1): ")
    sockets = input("Concurrent Sockets (default: 1): ")
    if url.startswith("https://"):
        url = "http://" + url[8:]
    if clouds is not None and clouds != "":
        clouds = "-c " + clouds
    if sockets is not None and sockets != "":
        sockets = "-s " + sockets
    file = os.path.join(os.path.dirname(__file__), "..", "scripts", "blackhorizon.py")
    os.system(f"python {file} {url} {clouds} {sockets}")
    os.system("cls" if os.name == "nt" else "clear")
    page_1()
    state.page = 1