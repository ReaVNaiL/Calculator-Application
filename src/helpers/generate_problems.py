from os import system
import random

class Problem:
    attempts_left: int = 3
    points = {
        "Easy": 1,
        "Medium": 3,
        "Hard": 5,
    }

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
    x = round(generate_random_number(m, n), 2)

    # Make sure that the problem is not a division by zero
    y = round((
        generate_random_number(m, n)
        if operator[0] != "/"
        else generate_random_number(1, n)
    ), 2)

    # Create the problem string
    problem = f"({x}) {operator[0]} ({y})"

    # Calculate the solution
    try:
        problem_solution = round(operator[1](x, y), 2)
    except:
        problem_solution = "Overflow Error"

    return Problem(problem, problem_solution)


# Test the generate_random_problem function
if __name__ == "__main__":
    system("cls")
    print(generate_random_problem("Easy"))
    print(generate_random_problem("Medium"))
    print(generate_random_problem("Hard"))
    print("\n\n")
