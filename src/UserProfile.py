from colorama import Fore, Back, Style
from consolemenu import *
from consolemenu.items import *

class Profile:
    score = 0
    problem_count = 0
    max_difficulty = "Easy"

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"> Name: {self.name}\n> Score: {self.score}\n> Problem Count: {self.problem_count}\n> Max Difficulty: {self.max_difficulty}"

    def update_score(self, score):
        self.score = score

class UserProfile:
    """
    This is the menu that will be displayed when the user selects the "User Profile" option from the main menu.
    Args:
        name (str): The name of the user
        main_menu (ConsoleMenu): The main menu that the user will be returned to after exiting this menu
        styling (MenuFormatBuilder): The styling for the menu
    Returns:
        SubmenuItem: The menu item that will be appended to the main menu
    """
    user = None
    def __new__(self, name: str, main_menu: ConsoleMenu, styling: MenuFormatBuilder) -> SubmenuItem:
        self.user = Profile(name, 0)
        profile_submenu = ConsoleMenu("User Profile", "View and edit your profile", formatter=styling)
        
        item1 = FunctionItem("Update Stats", self.update_user_stats, args=[self, profile_submenu])
        item2 = FunctionItem("Delete Stats", self.delete_user_stats, args=[self, profile_submenu])

        profile_submenu.append_item(item1)
        profile_submenu.append_item(item2)
        
        return SubmenuItem("User Profile", menu=main_menu, submenu=profile_submenu)
    
    def update_user_stats(self, menu: ConsoleMenu):
        # self.user.score = 23
        menu.prologue_text = self.user.__repr__()

        # input(Fore.GREEN + Back.BLACK + instructions)
        # print(Fore.LIGHTBLUE_EX)  # Reset the color
        
    def delete_user_stats(self, menu: ConsoleMenu):
        menu.prologue_text = "Stats deleted!"
        print(Fore.LIGHTBLUE_EX)
