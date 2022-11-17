TITLE = "main.py 1.00 2022/11/17"
"""
This file will execute Team Alpha's scheduling program.

Currently contains rudimentary tests.
"""

import Event_class
import menu

def main():
    #print("Bugger")
    #test = Event_class.Event_Schedule('Meeting', 2022, 11, 17, 17, 0, 'Discussing the project')
    #print(f"Today you have a {test.event_name}")

    choice = -1

    while choice != 5:
        choice = menu.printOptions()

if __name__ == '__main__':
    main()