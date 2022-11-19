from colorama import Fore, Back, Style
from consolemenu import *
from consolemenu.items import *
from src.helpers.generate_problems import *
from src.UserProfile import Profile


class ProblemsGen:
    """
    Class to generate a problem based on the difficulty.
    It includes the problem, the solution, and the number of attempts left.
    """

    curr_problem: Problem
    user: Profile

    def __new__(
        self, user: Profile, main_menu: ConsoleMenu, styling: MenuFormatBuilder
    ) -> SubmenuItem:
        problem_submenu = ConsoleMenu(
            "Problems", f"Select a {Fore.LIGHTYELLOW_EX}difficulty{Fore.LIGHTBLUE_EX} to begin...", formatter=styling
        )
        self.user = user
            
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
        """

        self.curr_problem = generate_random_problem(difficulty)
        prompt = f"What is the solution to {Fore.YELLOW}{self.curr_problem.problem}{Fore.CYAN}?"
        user_input = input(
            Fore.CYAN + prompt + "\nAnswer > " + Fore.YELLOW
        )

        # while has attempts left
        while self.curr_problem.attempts_left > 0:
            if self.curr_problem.check_solution(user_input):
                print(Fore.GREEN + "\nCorrect!")
                print(self.curr_problem.__repr__(), "\n")
                break
            else:
                print(Fore.RED + "Incorrect!", end=" ")

                print(
                    Fore.YELLOW
                    + f"You have {self.curr_problem.attempts_left} attempts left.\n"
                )
                self.curr_problem.decrease_attempts()

                user_input = input(
                    Fore.CYAN + prompt + "\nAnswer > " + Fore.YELLOW
                )

        if self.curr_problem.attempts_left == 0:
            print(
                Fore.RED
                + f"Game Over! The correct answer is {self.curr_problem.solution}.\n"
            )
        else:
            self.user.update_score(
                self.user.score + self.curr_problem.points[difficulty],
                self.user.problem_count + 1,
                difficulty,
            )

        input(Fore.LIGHTBLUE_EX + "Press enter to continue...")
        return self.curr_problem


if __name__ == "__main__":
    problems = ProblemsGen()
    problems.generate_problem("Easy")
