from colorama import Fore, Back, Style
from consolemenu import *
from consolemenu.items import *
import random
# from helpers.generate_problems import *


class Problem:
    attempts_left: int = 3

    def __init__(self, problem: str, solution):
        self.problem = problem
        self.solution = solution

    def __repr__(self):
        return f"{self.problem} = ({self.solution})"

    def check_solution(self, solution_arg: str):
        """
        Checks if the solution is correct

        Args:
            @solution_arg: The solution that the user entered
        """
        return str(self.solution) == solution_arg

    def decrease_attempts(self):
        self.attempts_left -= 1


def generate_random_operator():
    """
    Returns a random operation for basic algebra. ["+", "-", "*", "/", "^", "%", "//"]

    Returns:
        @operator: Tuple, (operator, function)
    """
    operators = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
        "%": lambda x, y: x % y,
        "^": lambda x, y: x**y,
        "//": lambda x, y: x // y,
    }

    return random.choice(list(operators.items()))


# Return a random number between
def generate_random_number(m, n):
    # If the numbers are integers check the type
    if type(m) == int and type(n) == int:
        return random.randint(m, n)

    # If the numbers are floats
    return random.uniform(m, n)


def generate_random_problem(difficulty: str) -> Problem:
    """
    Generates a random problem based on the difficulty
    - Easy: 2 digit numbers, 2 operators: addition and subtraction
    - Medium: 3 digit numbers, 4 operators: addition, subtraction, multiplication, and division
    - Hard: 4 digit numbers, all operators.
    """
    problem = ""
    problem_solution = 0
    m, n, x, y = 0, 0, 0, 0

    if difficulty == "Easy":
        m = 0
        n = 10
        # While the operator is not addition or subtraction
        while True:
            operator = generate_random_operator()
            if operator[0] in ["+", "-"]:
                break
    elif difficulty == "Medium":
        m = -100
        n = 100
        # While the operator is basic algebra
        while True:
            operator = generate_random_operator()
            if operator[0] in ["+", "-", "*", "/"]:
                break
    elif difficulty == "Hard":
        n = -1000.00
        m = 1000.00
        # Any operator
        operator = generate_random_operator()

    # Create a random problem
    x = generate_random_number(m, n)

    # Make sure that the problem is not a division by zero
    y = (
        generate_random_number(m, n)
        if operator[0] != "/"
        else generate_random_number(1, n)
    )

    # Create the problem string
    problem = f"({x}) {operator[0]} ({y})"

    # Calculate the solution
    try:
        problem_solution = round(operator[1](x, y), 2)
    except:
        problem_solution = "Overflow Error"

    return Problem(problem, problem_solution)


class ProblemsGen:
    """
    """
    curr_problem: Problem
    
    def __new__(self, main_menu: ConsoleMenu, styling: MenuFormatBuilder) -> SubmenuItem:
        problem_submenu = ConsoleMenu("Problems", "Select a difficulty to begin...", formatter=styling)
        
        easy = FunctionItem("Easy", self.generate_problem, args=[self, "Easy"])
        medium = FunctionItem("Medium", self.generate_problem, args=[self, "Medium"])
        hard = FunctionItem("Hard", self.generate_problem, args=[self, "Hard"])

        problem_submenu.append_item(easy)
        problem_submenu.append_item(medium)
        problem_submenu.append_item(hard)
        
        return SubmenuItem("Problems", menu=main_menu, submenu=problem_submenu)
    
    def generate_problem(self, difficulty: str) -> Problem:
        self.curr_problem = generate_random_problem(difficulty)
        prompt = f"What is the solution to {Fore.YELLOW}{self.curr_problem.problem}{Fore.CYAN}?"
        user_input = input(Fore.CYAN + Back.BLACK + prompt + "\nAnswer > " + Fore.YELLOW) 
        
        # while has attempts left
        while self.curr_problem.attempts_left > 0:
            if self.curr_problem.check_solution(user_input):
                print(Fore.GREEN + Back.BLACK + "\nCorrect!")
                print(self.curr_problem.__repr__(), "\n")
                break
            else:
                print(Fore.RED + Back.BLACK + "Incorrect!", end=" ")
                
                print(Fore.YELLOW + Back.BLACK + f"You have {self.curr_problem.attempts_left} attempts left.\n")
                self.curr_problem.decrease_attempts()
                
                user_input = input(Fore.CYAN + Back.BLACK + prompt + "\nAnswer > " + Fore.YELLOW)
        
        if self.curr_problem.attempts_left == 0:
            print(Fore.RED + Back.BLACK + f"Game Over! The correct answer is {self.curr_problem.solution}.\n")
            
        input(Fore.LIGHTBLUE_EX + Back.BLACK + "Press enter to continue...")
        return self.curr_problem
