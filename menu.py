TITLE = "menu.py 1.00 2022/11/17"
"""
This module contains functions for the
menu in the terminal.
"""
import Event_class

# Prints the default menu, and returns the user's
# selected option in the form of an integer
def printOptions():
    choice = input( "1. Schedule an event\n" \
                    "2. Delete an event\n" \
                    "3. Edit an event\n" \
                    "4. See your events\n" \
                    "5. Exit the program\n" \
                    "Please select an option by entering the number: ")
    return choice

# Asks for the name of an event from the user,
# and returns it. Error checks for entering blank spaces,
# quits when entering nothing
def getName():
    name = input("Please enter the name of the event: ")
    while name:

        # If name contains non-space characters, return name
        for c in name:
            if c != ' ': return name
        
        name = input("\nThe event name cannot be blank\n" \
                     "If you would like to cancel, press enter\n" \
                     "Please enter a valid event name: ")
    
    return name

# Creates an event object and stores it in a file.
# Calls getName, 
def createEvent():
    name = getName()

    if not name: 
        print("\nEvent creation cancelled")
        return False

    date = input("Please enter the date of the event: ")

    time = input("Please enter the time the event starts: ")

    details = input("Please enter any notes about the event you'd like to remember: ")

if __name__ == '__main__':
    createEvent()