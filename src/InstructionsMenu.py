import colorama as c
from consolemenu import *
from consolemenu.items import *
from consolemenu.format import *


class InstructionsMenu:
    """
    Creates the instructions menu.
    @return: Returns the instructions menu object.
    """

    def __new__(self) -> FunctionItem:
        # Read instructions File.
        with open("./data/app_instructions.txt", "r") as f:
            instructions = f.read()

        # Set the menu to green on black
        instructions_item = FunctionItem(
            "Instructions", self.show_instructions, [self, instructions]
        )

        return instructions_item

    def show_instructions(self, instructions):
        input(c.Fore.GREEN + c.Back.BLACK + instructions)
        print(c.Fore.LIGHTBLUE_EX)  # Reset the color
