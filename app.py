import colorama as c
from consolemenu import *
from consolemenu.items import *
from consolemenu.format import *
from models.UserProfile import UserProfile as up
import models.InstructionsMenu as im

def start_menu():
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
    main_menu_format = MenuFormatBuilder().set_border_style_type(MenuBorderStyleType.HEAVY_BORDER) \
        .set_prompt(">") \
        .set_title_align('center') \
        .set_subtitle_align('center') \
        .set_left_margin(4) \
        .show_header_bottom_border(True)
    
    # Create the menu
    menu = ConsoleMenu("Practical Math Application", "A program to help you practice your math skills!", formatter=main_menu_format)
    
    # Create 3 Submenus
    profile_submenu = ConsoleMenu("User Profile", "View and edit your profile")
    problems_submenu = ConsoleMenu("Problems", "View and edit your problems")
    
    # Create the menu items
    profile_item = SubmenuItem("User Profile", submenu=profile_submenu)
    problems_item = SubmenuItem("Problems", submenu=problems_submenu)
    instructions_item = im.InstructionsMenu()
    
    # Append the menu items to the main menu
    menu.append_item(profile_item)
    menu.append_item(problems_item)
    menu.append_item(instructions_item)
    
    # Create some items
    print(c.Fore.LIGHTBLUE_EX)
    c.init(autoreset=False)
    menu.show() 

if __name__ == "__main__":
    start_menu()