from func.pages import page_1
from func.pages import page_2
from func.pages import page_3
# define main page

class StateManager:
    def __init__(self):
        self.page = 1
state = StateManager()
pages = {
    1: page_1,
    2: page_2,
    3: page_3,
}