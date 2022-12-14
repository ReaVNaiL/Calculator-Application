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
        self.rounded_solution = round(solution, 2)

    def __repr__(self):
        return f"{self.problem} = ({self.rounded_solution})"

    def check_solution(self, solution_arg: float):
        """
        Checks if the solution is correct

        Args:
            @solution_arg: The solution that the user entered
        """
        rounded_solution_arg = round(solution_arg, 2)
        
        return solution_arg == self.rounded_solution or rounded_solution_arg == self.rounded_solution or solution_arg == self.solution

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


def generate_random_number(m, n):
    # If the numbers are integers check the type
    if type(m) == int and type(n) == int:
        return random.randint(m, n)

    # If the numbers are floats
    return random.uniform(m, n)


def get_difficulty_values(difficulty: str):
    m, n, x, y = 0, 0, 0, 1

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
    y = round((generate_random_number(m, n)), 2)

    # Make sure that the problem is not a division by zero x / 0
    if y == 0 and operator[0] == "/" or operator[0] == "//":
        round(generate_random_number(1, n + 1), 2)

    # if operator[0] == "^" and y < -1 or y > 20 keep the operator
    # else generate a new y value between 0 and 20
    if operator[0] == "^" and y < -1 or y > 20:
        y = round(generate_random_number(1, 5), 2)

    return (x, y, operator)


def generate_random_problem(difficulty: str) -> Problem:
    """
    Generates a random problem based on the difficulty
    - Easy: 2 digit numbers, 2 operators: addition and subtraction
    - Medium: 3 digit numbers, 4 operators: addition, subtraction, multiplication, and division
    - Hard: 4 digit numbers, all operators.
    """
    problem = ""
    problem_solution = 0

    # Generate the values for the problem
    x, y, operator = get_difficulty_values(difficulty)

    # Create the problem string
    problem = f"({x}) {operator[0]} ({y})"

    # Calculate the solution
    try:
        problem_solution = operator[1](x, y)
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
