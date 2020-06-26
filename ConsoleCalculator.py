# Calculator
"""
My calculator contains a basic arithmetic function which performs math operations on two numbers and a calculator
function which takes in a mathematical equation as a string argument and outputs the numbers.

This calculator can calculate any amount of numerical terms.

This calculator takes into account precedence of operators (exponentials first, then multiply and divide, and finally
addition and subtraction). This calculator can also interpret precedence through brackets (eg. (x+y)/z will evaluate
(x+y) first.)
"""

# the calc() function is used to evaluate a two term expression using basic python operators. It takes two numbers as
# the first two arguments and a operator character to denote which operation to evaluate.


def calc(num1, num2, op):
    op = op.upper()
    if op == "A":
        return num1 + num2
    elif op == "S":
        return num1 - num2
    elif op == "M":
        return num1 * num2
    elif op == "D":
        if num2 == 0:
            # print("Cannot divide by zero!")
            return "Undefined"
        else:
            return num1 / num2
    elif op == "P":
        return pow(num1, num2)
    else:
        print("Operators can only be 'A', 'S', 'M', 'D' or 'P'")
        return

# the calculate() function uses the basic calc() function to evaluate multi-term math expressions. It takes a single
# string input containing a math expression. This can contain common math operators: *, /, +, - and ^ as well as
# special characters such as '(', ')', '.' as well as '+' and '-' when used as sign prefixes. This function will take
# operator precedence into account as well as precedence due to brackets.


def calculate(formula):
    formula = formula.replace(" ", "")  # This deletes whitespaces in the formula
    numbers = []    # This list contains the integer values extracted from the string
    op = []     # This list contains the math operator values to be sent to the calc() function
    num_str = ""   # This is the string buffer for extracting the numerical terms from the formula string.
    brackets = True     # This will evaluate to false if there are no brackets or if all bracket terms are evaluated
    signed = False  # Will evaluate to true if a signed number proceeds a math operator. This is to avoid false op
                    # readings.
    while brackets:
        sign_change = False
        if "(" in formula and ")" in formula:
            if formula.count("(") != formula.count(")"):
                print("Uneven braces in equation!")
                return
            else:
                open_bracket = formula.index("(")   # Save open bracket index as start of bracket term.
                for b in range(open_bracket, len(formula)):
                    if formula[b + 1] == "(":   # Check next element for another bracket of greater precedence.
                        open_bracket = b + 1    # Save new index as start of bracket term.

                    elif formula[b + 1] == ")":  # Check for close bracket. If close bracket is found, save its index
                        close_bracket = b + 1
                        break

                temp = formula  # save copy of input string
                formula = formula[open_bracket + 1:close_bracket]   # make new string containing just bracket term.
        else:
            brackets = False
        # If bracket term is established, then only bracket term will be evaluated and the numbers will replace the
        # bracket term in the original formula string. This process will repeat until all bracket terms are evaluated
        # and replaced by their results.
        for j in range(len(formula)):
            if formula.find("--") > 0:
                temp1 = formula.split('--')
                formula = "+".join(temp1[0:])
                sign_change = True
                brackets = True
                break
            if formula.find("+-") > 0:
                temp1 = formula.split('+-')
                formula = "-".join(temp1[0:])
                sign_change = True
                brackets = True
                break
            if formula.find("-+") > 0:
                temp1 = formula.split('-+')
                formula = "-".join(temp1[0:])
                sign_change = True
                brackets = True
                break
            if formula[j].isdigit() or formula[j] == ".":   # Will add element to num_str buffer if it is a valid
                num_str += formula[j]                          # numerical value.

            elif (formula[j] == "+" or formula[j] == "-") and j == 0:   # Will take into account sign value.
                num_str += formula[j]

            else:                               # If operator character is reached, this indicates end of numerical term
                if num_str:                        # and the value will be copied to the numbers[] list.
                    numbers.append(float(num_str))
                    num_str = ""
                if formula[j] == "+":           # Operator will be added to op[] list to determine what operation to
                    if signed:                  # conduct and in which order.
                        num_str = formula[j]
                        signed = False
                    else:
                        op.append("A")             
                elif formula[j] == "-":
                    if signed:
                        num_str = formula[j]
                        signed = False
                    else:
                        op.append("S")
                elif formula[j] == "*":
                    op.append("M")
                elif formula[j] == "/":
                    op.append("D")
                elif formula[j] == "^":
                    op.append("P")
                else:
                    print("Invalid math operator")
                    return
                if formula[j + 1] == "-" or formula[j + 1] == "+":
                    signed = True

        try:
            numbers.append(float(num_str))  # Needed here to add final numerical term in equation.
        except ValueError:
            None
        num_str = ""   # In case of brackets, num_str buffer needs to be cleared if function needs to loop.
        # The three lower lines are used to debug.
        # print(numbers)
        # print(op)
        # print(op_str)
        while "P" in op:    # Order of these while loops are important for math operation precendence.
            i = op.index("P")
            numbers[i] = calc(numbers[i], numbers[i + 1], "P")
            numbers.remove(numbers[i + 1])
            op.remove(op[i])    # Once operator is used, it is removed from op[] list.
        while "D" in op:        # This is repeated until there are only '+' and '-' operators left.
            i = op.index("D")
            numbers[i] = calc(numbers[i], numbers[i + 1], "D")
            if numbers[i] == "Undefined":
                return "Undefined"
            numbers.remove(numbers[i + 1])
            op.remove(op[i])
        while "M" in op:
            i = op.index("M")
            numbers[i] = calc(numbers[i], numbers[i + 1], "M")
            numbers.remove(numbers[i + 1])
            op.remove(op[i])
        for k in range(len(op)):
            numbers[0] = calc(numbers[0], numbers[1], op[k])
            numbers.remove(numbers[1])
        if brackets:
            if not sign_change:
                temp = temp.replace(temp[open_bracket:close_bracket + 1], str(numbers[0]))
                formula = temp
            numbers.clear()
            op.clear()
    return numbers[0]


""" UNCOMMENT THIS SECTION TO RUN THROUGH PYTHON CONSOLE OR LEAVE COMMENTED TO USE THE CALCULATOR FUNCTIONS AS A MODULE FOR ANOTHER PROGRAM.
run = True
while run:
    x = input("Please enter calculation: ")
    if x == 'q':
        run = False
    elif x:
        y = calculate(x)
        print(y)
"""
