# IMPORTED RANDOM TO GENERATE NUMBERS
# I HAD TO IMPORT OPERATOR BI'S TO CONVERT STR TO OP'S USING A DICT.

import random
import operator

opseta = {0: operator.truediv, 1: operator.mul, 2: operator.add,
         3: operator.sub, 4: operator.mod, 5: operator.floordiv}
opsetb = ("/", "*", "+", "-", "%", "//")
tester = ''
mod = ''
ct = ''
uct = ''
retry = ''
results = {}

# TA-DA! THE HEART OF OUR PROGRAM. LESS THAN 10 LINES OF CODE LOL
def generate():
    while ct <= uct:
        varA = random.randint(0, 99)
        varB = random.randint(0, 99)
        mod = [random.randint(0, 5)]
        for mod in opseta:
            continue
        problem = varA, varB
        sol = ''
        print(problem, sol)

#I WROTE THIS FIRST, SO ITS FLOATING UNTIL I GET TO IT.
'''
    usersol = ""
    retry = ""
    # "//" how many times will x go into y without a fraction, do not show remainder.
    # "%" What is the remainder of x divided by y.
    usersol = input("Solve the following: ", varA, operator, varB)
    while usersol != answer:
        print("Oh no, that's not the correct answer!")
        retry = input("Try Again?")
        if retry == "yes":
            usersol = input("Solve the following: ", varA, operator, varB)
        else:
            print("That's correct! Great job!")
            continue
'''
#PROGRAM STARTS HERE!!!!!!!!!!
if __name__ == '__main__':
    tester = input("What is your name? ")
    ct = 1
    uct = int(input("How many problems would you like to complete?"))
    retry = int(input("How many attempts would you like per question? (Max 3)"))
    if retry > 3:
        retry = 3
    else:
        pass
    generate()