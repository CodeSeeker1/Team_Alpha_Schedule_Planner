TITLE = "Event_list.py 1.01 2022-11-19"
"""-----------------------------------------------------
Functions to add, delete, and sort
a list of Event_Schedule objects.

Also includes reading data from a file
to the list, and writing data from the list to
a file.
-------------------------------------------------------"""
#---------------------------------------------------------
# Imports
import Event_class

#---------------------------------------------------------
# Comparisons, may move to class
def dateToInt(event):
    """
    Passed an Event_Schedule obj and returns an integer
    with the year, month, day, hour, and minute.

    Ex. Nov 19, 2022 12:33pm becomes: 202211191233

    Used for date and time comparison.
    """
    date = event.get_date()
    time = event.get_time()

    integer =  date[0] * 100000000 + date[1] * 1000000 + date[2] * 10000
    integer += time[0] * 100 + time[1]

    return integer

def earlier(lEvent, rEvent):
    "Returns True if lEvent is before rEvent"
    return dateToInt(lEvent) < dateToInt(rEvent)

def equals(lEvent, rEvent):
    "Returns True if lEvent happens at the same time as rEvent"
    return dateToInt(lEvent) == dateToInt(rEvent)

def later(lEvent, rEvent):
    "Returns True if lEvent is after rEvent"
    return dateToInt(lEvent) > dateToInt(rEvent)

#--------------------------------------------------------
# Adding, searching, deleting and updating
def addEvent(elist, event):
    """
    elist is a list of events, event is an Event_Schedule obj.
    Adds event object to list and sorts it based on date and time.
    """
    elist.append(event)
    elist.sort(key=dateToInt)

def findTime(elist, key):
    """
    elist is a list of events and key is the time 
    integer of the event.
    It is assumed elist is sorted by date and time.

    Returns the index of the matching time.

    Planning to modify it to return a list of indices, in
    case several events have the same name or time.
    """
    x = "donothing"


def findName(elist, key):
    """
    elist is a list of events and key is the string of
    the event name.
    It is assumed elist is sorted by date and time.

    Returns the index of the matching string.

    Planning to modify it to return a list of indices, in
    case several events have the same name or time.
    """
    l = elist.copy()
    x = "donothing"

#--------------------------------------------------------
# Testing
if __name__ == '__main__':
    print(TITLE)

    l = []
    e = Event_class.Event_Schedule("Class", 2022, 11, 19, 14, 20, "Hell in a handbasket")
    v = Event_class.Event_Schedule("Vacay", 2022, 11, 21, 12, 20, "Cya l8r losers")
    n = Event_class.Event_Schedule("Board", 2022, 11, 21, 12, 20, "Be early")
    t = Event_class.Event_Schedule("Wakup", 2022, 11, 21,  7, 30, "Bacon 4 brkfst")
    
    print()

    print("Testing dateToInt:")
    print(dateToInt(e))

    print()

    print("Testing comparisons:")
    print(earlier(e, v), equals(e, v), later(e, v))
    print(earlier(v, n), equals(v, n), later(v, n))
    print(earlier(n, t), equals(n, t), later(n, t))

    print()

    print("Testing addEvent:")
    addEvent(l, v)
    addEvent(l, e)
    addEvent(l, n)
    addEvent(l, t)
    for i in range(len(l)):
        print(l[i].event_name)
    
    print()

    print("Testing findTime")
    


