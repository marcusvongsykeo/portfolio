# Simple function which determines whether brackets in a string are paired correctly 
# (if each open bracket has a paired closed bracket in the correct order of precedence.)
# This function is inspired from an example of an implementation of a stack by William Fiset 
# on his 'Data Structures and Algorithms' videos on YouTube: https://www.youtube.com/watch?v=RBSGKlAvoiM

def bracket_check(bracket_set):
    brack_stack = []
    openbrack = "([{"
    closebrack = ")]}"
    for current in bracket_set:
        if current in openbrack:
            brack_stack.append(current)
        elif current in closebrack:
            if current == ")" and brack_stack[-1] == "(":
                brack_stack.pop(-1)
            elif current == "]" and brack_stack[-1] == "[":
                brack_stack.pop(-1)
            elif current == "}" and brack_stack[-1] == "{":
                brack_stack.pop(-1)
            elif current == ")" and brack_stack[-1] == "(":
                brack_stack.pop(-1)
            else:
                return "Invalid Set!"
    if brack_stack:
        return "Invalid Set!"
    else:
        return "Set is Valid!"


# Sample program to demonstrate functionality.
bracket_string = "[]({{[]}}})"
print(bracket_check(bracket_string))
