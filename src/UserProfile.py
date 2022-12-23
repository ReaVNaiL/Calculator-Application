from colorama import Fore, Back, Style
from consolemenu import *
from consolemenu.items import *
import os
import pandas as pd
import numpy as np

csv_path = os.path.join(os.path.dirname(__file__), "..\\data\\user_data.csv")


class Profile:
    score = 0
    problem_count = 0
    max_difficulty = "Easy"
    diff_scale = {
        "Easy": 1,
        "Medium": 2,
        "Hard": 3,
    }
    _user_id = 0

    def __init__(self, name):
        self.name = name

        if os.path.exists(csv_path):
            self._user_id = self.get_user_id()
            if self._user_id == 0:
                self._user_id = self.generate_user_id()
            else:
                self._user_id = self.generate_user_id()

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

    def generate_user_id(self):
        """
        This function will generate a unique user_id for the user.
        If the user_id is not unique, it will recursively call itself until a unique user_id is generated.
        Returns:
            int: A unique user_id
        """
        # Generate a unix user_id
        self._user_id = np.random.randint(100000, 999999)

        # Check if the user_id is unique
        data = pd.read_csv(csv_path)
        if self._user_id in data["user_id"].values:
            return self.generate_user_id()

        return self._user_id

    def get_user_id(self):
        df = pd.read_csv(csv_path)

        if self.name in df["user_name"].values:
            return df[df["user_name"] == self.name]["user_id"].values[0]

        return self._user_id


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
    # get file path using os.path.join and current directory
    csv_path = os.path.join(os.path.dirname(__file__), "..\\data\\user_data.csv")

    def __init__(self, user: Profile, main_menu: ConsoleMenu, styling: MenuFormatBuilder):
        profile_submenu = ConsoleMenu(
            f"{Fore.LIGHTYELLOW_EX}{user.name}{Fore.LIGHTBLUE_EX}'s Profile",
            f"View and edit your {Fore.LIGHTYELLOW_EX}profile{Fore.LIGHTBLUE_EX}",
            formatter=styling,
        )

        # Encapsulate the user profile menu in a submenu
        self.user = user
        self.profile_console = profile_submenu
        self.import_user_stats()
        self.update_user_stats(profile_submenu)
        

        item1 = FunctionItem("Export Stats", self.export_user_stats, args=[])
        item2 = FunctionItem("Import Stats", self.import_user_stats, args=[])
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
        menu.prologue_text = "Local Stats Deleted!"

        self.user.score = 0
        self.user.problem_count = 0
        self.user.max_difficulty = "Easy"

        print(Fore.LIGHTBLUE_EX)

    def export_user_stats(self):
        """
        CSV Data is stored in the following format:
            name, score, max_difficulty, percentage_completed
            daniel, 123, 100, 10, 100
        """
        # use pandas to write to csv file
        df = pd.read_csv(csv_path)

        # If the user does not exist, create a new row for them
        if not self.user_exists(df):
            self.create_user(df)

        row = df.loc[df["user_name"] == self.user.name]

        if row.empty:
            print("User not found!")
            return
        
        # Update the user's row
        df.loc[row.index, "score"] = self.user.score
        df.loc[row.index, "max_difficulty"] = self.user.max_difficulty
        df.loc[row.index, "problem_count"] = self.user.problem_count

        # Write the data to the csv file
        df.to_csv(csv_path, index=False)

    def import_user_stats(self):
        """
        This function will import the user's stats from the csv file.
        """
        # use pandas to read csv file
        df = pd.read_csv(csv_path)
        
        # Look for the user in the csv file
        row = df.loc[df["user_name"] == self.user.name]
        
        if row.empty:
            print("User not found!")
            return
        
        # Update the user's stats
        self.user.score = row["score"].values[0]
        self.user.max_difficulty = row["max_difficulty"].values[0]
        self.user.problem_count = row["problem_count"].values[0]
        
        # Update the user's stats in the menu
        self.update_user_stats(self.profile_console)

    def user_exists(self, data: pd.DataFrame) -> bool:
        """
        This function will check if the user exists in the csv file.

        Returns:
            bool: True if the user exists, False otherwise
        """
        try:
            if self.user._user_id in data["user_id"].values:
                return True
        except:
            pass

        return False

    def create_user(self, data: pd.DataFrame):

        # Create a new row for the user
        new_row = pd.DataFrame(
            [[self.user._user_id, self.user.name, self.user.score, self.user.max_difficulty, self.user.problem_count]],
            columns=["user_id", "user_name", "score", "max_difficulty", "problem_count"],
        )

        data = data.append(new_row, ignore_index=True)

        # Write the data to the csv file
        data.to_csv(csv_path, index=False)