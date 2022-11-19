from os import system
import colorama as c
from consolemenu import *
from consolemenu.items import *
from consolemenu.format import *
import src.UserProfile as up
import src.InstructionsMenu as im
import src.ProblemsGen as pg


def start_menu(user_name: str):
    # Create a menu that looks like this:
    # +------------------+
    # | Title Menu       |
    # | Menu Subtitle    |
    # +------------------+
    # | 1. User Profile  |
    # | 2. Problems      |
    # | 3. Instructions  |
    # | 4. Exit          |
    # +------------------+

    # Formats the header
    main_menu_format = (
        MenuFormatBuilder()
        .set_border_style_type(MenuBorderStyleType.HEAVY_BORDER)
        .set_prompt(">")
        .set_title_align("center")
        .set_subtitle_align("center")
        .set_left_margin(4)
        .show_header_bottom_border(True)
    )

    # Create the menu
    menu = ConsoleMenu(
        "Practical Math Application",
        f"Hi {c.Fore.LIGHTYELLOW_EX}{user_name}{c.Fore.LIGHTBLUE_EX}!\nA program to help you practice your math skills!",
        formatter=main_menu_format,
    )
    
    # Assign the user profile to a variable
    user_profile = up.Profile(user_name)

    # Create 3 Submenus
    profile_item = up.UserProfile(user_profile, menu, main_menu_format)
    profile_item.set_menu(menu)
    
    problems_item = pg.ProblemsGen(user_profile, menu, main_menu_format)
    
    instructions_item = im.InstructionsMenu()

    # Append the menu items to the main menu
    menu.append_item(profile_item)
    menu.append_item(problems_item)
    menu.append_item(instructions_item)

    # Create some items
    print(c.Fore.LIGHTBLUE_EX)
    c.init(autoreset=False)
    menu.start()
    menu.join()


if __name__ == "__main__":
    system("cls")
    # name = input(c.Fore.LIGHTYELLOW_EX + "Hello! Please enter your name: ")
    name = "John"
    start_menu(name)
