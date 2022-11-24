from colorama import Fore, Back, Style
from consolemenu import *
from consolemenu.items import *
from src.helpers.generate_problems import *
from src.UserProfile import Profile, UserProfile


class ProblemsGen:
    """
    Class to generate a problem based on the difficulty.
    It includes the problem, the solution, and the number of attempts left.
    
    Args:
        @param user: The user's profile
        @param profile_submenu: The user's profile submenu
        @param main_menu: The main menu
        @param styling: The styling for the submenu
    
    Returns:
        @return problem_submenu: The problem submenu
    """

    curr_problem: Problem
    user: Profile
    profile_submenu: UserProfile

    def __new__(self, user: Profile, profile_submenu: UserProfile, main_menu: ConsoleMenu, styling: MenuFormatBuilder) -> SubmenuItem:
        # Set Up Problems Menu
        problem_submenu = ConsoleMenu(
            "Problems",
            f"Select a {Fore.LIGHTYELLOW_EX}difficulty{Fore.LIGHTBLUE_EX} to begin...",
            formatter=styling
        )
        
        # Encapsulate User Profile
        self.user = user
        self.profile_submenu = profile_submenu

        easy = FunctionItem("Easy", self.generate_problem, args=[self, "Easy"])
        medium = FunctionItem("Medium", self.generate_problem, args=[self, "Medium"])
        hard = FunctionItem("Hard", self.generate_problem, args=[self, "Hard"])

        problem_submenu.append_item(easy)
        problem_submenu.append_item(medium)
        problem_submenu.append_item(hard)

        return SubmenuItem("Problems", menu=main_menu, submenu=problem_submenu)

    def generate_problem(self, difficulty: str) -> Problem:
        """
        Generate a problem based on the difficulty.
        It will then display the problem and ask for the user's answer.
        Initially, the problem will be generated randomly, and you will be given 3 tries to get the correct answer.
        
        Args:
            @param difficulty: The difficulty of the problem
        """
        self.curr_problem = generate_random_problem(difficulty)

        user_input = self.prompt_user(self.curr_problem.problem)
        
        # while has attempts left
        while self.curr_problem.attempts_left > 0:
            if self.curr_problem.check_solution(user_input):
                print(Fore.GREEN + "\nCorrect!")
                print(self.curr_problem.__repr__(), "\n")
                break
            else:
                # Display the number of attempts left
                print(Fore.RED + "Incorrect!", end=" ")
                print(Fore.YELLOW + f"You have {self.curr_problem.attempts_left} attempts left.\n")
                self.curr_problem.decrease_attempts()
                # Ask For Input Again.
                user_input = self.prompt_user()

        # If the user has no attempts left, display the correct answer.
        # Or if the user has answered correctly, display the correct answer.
        # As well as update the user's profile.
        if self.curr_problem.attempts_left == 0:
            print(Fore.RED + f"Game Over! The correct answer is {self.curr_problem.solution}.\n")
        else:
            self.profile_submenu.update_user_stats(self.profile_submenu.submenu)
            self.user.update_score(
                self.user.score + self.curr_problem.points[difficulty],
                self.user.problem_count + 1,
                difficulty
            )

        input(Fore.LIGHTBLUE_EX + "Press enter to continue...")
        return self.curr_problem

    def prompt_user(problem) -> str:
        """
        Prompt the user for their answer.
        
        Args:
            @param problem: The problem to be displayed
        """
        prompt = f"What is the solution to {Fore.YELLOW}{problem}{Fore.CYAN}?"
        
        # while not numeric input print error message and ask for input again
        user_input = input(Fore.CYAN + prompt + "\nAnswer > " + Fore.YELLOW).strip()
        
        while user_input.isalpha() or user_input == "":
            print(Fore.RED + "\nYour answer can only contain numbers. Please try again...\n")
            user_input = input(Fore.CYAN + prompt + "\nAnswer > " + Fore.YELLOW)
        
        return user_input

if __name__ == "__main__":
    problems = ProblemsGen()
    problems.generate_problem("Easy")
