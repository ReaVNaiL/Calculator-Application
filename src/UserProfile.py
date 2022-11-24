from colorama import Fore, Back, Style
from consolemenu import *
from consolemenu.items import *


class Profile:
    score = 0
    problem_count = 0
    max_difficulty = "Easy"
    diff_scale = {
        "Easy": 1,
        "Medium": 2,
        "Hard": 3,
    }

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return (
              f"> Name: {Fore.LIGHTYELLOW_EX}{self.name}{Fore.LIGHTBLUE_EX}\n"
            + f"> Score: {Fore.LIGHTYELLOW_EX}{self.score}{Fore.LIGHTBLUE_EX}\n"
            + f"> Problem Count: {Fore.LIGHTYELLOW_EX}{self.problem_count}{Fore.LIGHTBLUE_EX}\n"
            + f"> Max Difficulty: {Fore.LIGHTGREEN_EX}{self.max_difficulty}{Fore.LIGHTBLUE_EX}\n"
        )

    def update_score(self, score, problem_count, max_difficulty):
        self.score = score
        self.problem_count = problem_count
        
        if self.diff_scale[max_difficulty] > self.diff_scale[self.max_difficulty]:
            self.max_difficulty = max_difficulty

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
    submenu: SubmenuItem
    profile_console: ConsoleMenu

    def __init__(self, user: Profile, main_menu: ConsoleMenu, styling: MenuFormatBuilder):
        profile_submenu = ConsoleMenu(
            f"{Fore.LIGHTYELLOW_EX}{user.name}{Fore.LIGHTBLUE_EX}'s Profile",
            f"View and edit your {Fore.LIGHTYELLOW_EX}profile{Fore.LIGHTBLUE_EX}",
            formatter=styling,
        )
        
        # Encapsulate the user profile menu in a submenu
        self.user = user
        self.profile_console = profile_submenu
        self.update_user_stats(profile_submenu)
        
        
        item1 = FunctionItem("Export Stats *TBD*", self.export_user_stats, args=[])
        item2 = FunctionItem("Import Stats *TBD*", self.delete_user_stats, args=[profile_submenu])
        item3 = FunctionItem("Delete Stats", self.delete_user_stats, args=[profile_submenu])

        profile_submenu.append_item(item1)
        profile_submenu.append_item(item2)
        profile_submenu.append_item(item3)

        self.submenu = SubmenuItem("User Profile", menu=main_menu, submenu=profile_submenu)

    def update_user_stats(self, menu: ConsoleMenu):
        """
        This function will update the user's stats and display them in the menu.
        
        Args:
            menu (ConsoleMenu): The menu that will be updated
        """
        menu.prologue_text = self.user.__repr__()
        print(Fore.LIGHTBLUE_EX)  # Reset the color

    def delete_user_stats(self, menu: ConsoleMenu):
        menu.prologue_text = "Stats deleted!"

        self.user.score = 0
        self.user.problem_count = 0
        self.user.max_difficulty = "Easy"

        print(Fore.LIGHTBLUE_EX)
        
    def export_user_stats(self):
        """
        TBD
        """
        pass
    
    def import_user_stats(self):
        """
        TBD
        """
        pass
    
