#!/usr/bin/python
#

"""
    Stack usage examples - Paranthesis Checker

    Pass a string with '(' and ')' it will ensure they are balanced pairs

    Returns True if they match, False if they do not, it will print an 
    '^' to show the position that is missing
"""
from pystack import pystack
from pyansi  import print_colour, print_reset, FG_RED

mystack = pystack(20)

def ParenthesisMatch(string_to_parse):
    """
        ParenthesisMatch

        Parse the string paramater and balance pairs of
        '(' and ')'

        Returns True is matched, False otherwise
    """
    charpos = 0
    check = True

    print_reset()
    
    for letter in string_to_parse:
        if letter == '(':
            mystack.push(letter)
        elif (not mystack.isEmpty() and letter == ')') and mystack.peek() == '(':
            mystack.pop()
        else:
            check = False
            break
        charpos = charpos + 1

    if check and mystack.isEmpty():
        return True
    else:
        print(string_to_parse)
        for i in range(charpos):
            print(" ", end='')
#        print("^\n")
        print_colour(FG_RED, "^")

        return False

if __name__ == '__main__':
    print("Parenthesis Checker")

    Exp1 = "()"
    if ParenthesisMatch(Exp1):
        print(Exp1 + "  Matches")

    Exp2 = "(())"
    if ParenthesisMatch(Exp2):
        print(Exp2 + "  Matches")

    Exp3 = "(((((())))))"
    if ParenthesisMatch(Exp3):
        print(Exp3 + "  Matches")

    Exp4 = "("
    if ParenthesisMatch(Exp4):
        print(Exp4 + "  Matches")

    Exp5 = "(()"
    if ParenthesisMatch(Exp5):
        print(Exp5 + "  Matches")

    Exp6 = "(()))"
    if ParenthesisMatch(Exp6):
        print(Exp6 + "  Matches")

    Exp7 = "(((((((()))";
    if ParenthesisMatch(Exp7):
        print(Exp7 + "  Matches")
    
    Exp8 = "())))))))";
    if ParenthesisMatch(Exp8):
        print(Exp8 + "  Matches")

    print_reset()
