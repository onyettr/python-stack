#!/usr/bin/python
#pylint: disable=invalid-name
#pylint: disable=superfluous-parens
"""
   python ANSI Terminal sequences
"""

#
# Character colours
#
FG_BLACK = 30
FG_RED = 31
FG_GREEN = 32
FG_YELLOW = 33
FG_BLUE = 34
FG_MAGENTA = 35
FG_CYAN = 36
FG_WHITE = 37

# ANSI Escape sequences
ESCAPE = "\033[0;"
RESET_SEQ = "\033[m"

def print_reset():
   """output screen reset sequence"""
   print(RESET_SEQ)

def print_colour(colour, msg):
    """output screen colour sequence"""
    print(ESCAPE + str(colour) + 'm' + msg)
