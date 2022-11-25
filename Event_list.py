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

def sort_dateToInt(event):
    "Returns the datToInt of event. Used for sorting"
    return event.dateToInt()

def earlier(lEvent, rEvent):
    "Returns True if lEvent is before rEvent"
    return lEvent.dateToInt() < rEvent.dateToInt()

def equals(lEvent, rEvent):
    "Returns True if lEvent happens at the same time as rEvent"
    return lEvent.dateToInt() == rEvent.dateToInt()

def later(lEvent, rEvent):
    "Returns True if lEvent is after rEvent"
    return lEvent.dateToInt() > rEvent.dateToInt()

#--------------------------------------------------------
# Adding, searching, deleting and updating
def addEvent(elist,name,year,month,day,hour,minute,details):
    """
    elist is a list of events. 
    Other parameters correspond to the parameters of an Event_Schedule object. 
    Will add error checking for each parameter!

    Adds event object to list and sorts it based on date and time.
    returns index of event object.
    """
    event = Event_class.Event_Schedule(name,year,month,day,hour,minute,details)
    elist.append(event)
    elist.sort(key=sort_dateToInt)

    return findName(elist, name)

def findTime(elist, key):
    """
    elist is a list of events.
    key is the time integer of the event.
    It is assumed elist is sorted by date and time.

    Returns the index of the matching time.

    May build a more efficient binary search if time permits.
    """
    for i in range(len(elist)):
        if elist[i].dateToInt == key:
            return i


def findName(elist, key):
    """
    elist is a list of events.
    key is the time integer of the event.
    It is assumed elist is sorted by date and time.

    Returns the index of the matching time.

    May build a more efficient binary search if time permits.
    """
    for i in range(len(elist)):
        if elist[i].event_name == key:
            return i

#--------------------------------------------------------
# File communication
def eventToDict(event):
    '''
    Turns an event object into a dictionary. 
    Used to create a dictionary for file writing.
    '''
    date = event.get_date()
    time = event.get_time()

    dictionary = {'name':event.name, 'year':date[0], 'month':date[1], 'day':date[2], \
                  'hour':time[0],'minute':time[1], 'details':event.details}

    return dictionary

#--------------------------------------------------------
# Testing
if __name__ == '__main__':
    print(TITLE)

    l = []
    e = l[addEvent(l, "Class", 2022, 11, 19, 14, 20, "Hell in a handbasket")]
    v = l[addEvent(l, "Vacay", 2022, 11, 21, 12, 20, "Cya l8r losers")]
    n = l[addEvent(l, "Board", 2022, 11, 21, 12, 20, "Be early")]
    t = l[addEvent(l, "Wakup", 2022, 11, 21,  7, 30, "Bacon 4 brkfst")]
    
    print()

    print("Testing dateToInt:")
    print(e.dateToInt())

    print()

    print("Testing comparisons:")
    print(earlier(e, v), equals(e, v), later(e, v))
    print(earlier(v, n), equals(v, n), later(v, n))
    print(earlier(n, t), equals(n, t), later(n, t))

    print()

    print("Testing addEvent:")
    for i in range(len(l)):
        print(l[i].event_name)
    
    print()

    print("Testing findTime")
    


