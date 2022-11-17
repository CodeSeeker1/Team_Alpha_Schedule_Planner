TITLE = "menu.py 1.00 2022/11/17"
"""
This module contains functions for the
menu in the terminal.
"""

# Prints the default menu, and returns the user's
# selected option in the form of an integer
def printOptions():
    choice = input( "1. Schedule an event\n" \
                    "2. Delete an event\n" \
                    "3. Edit an event\n" \
                    "4. See your events\n" \
                    "5. Exit the program\n" \
                    "Please select an option by entering the number: ")
    return int(choice)