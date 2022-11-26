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
    return str(event.dateToInt())

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
# Adding, searching, deleting and editing
def addEvent(elist, name, date, time, details):
    """
    elist is a list of events. 
    Other parameters correspond to the parameters of an Event_Schedule object. 
    Will add error checking for each parameter!

    Adds event object to list and sorts it based on date and time.
    returns index of event object.
    """
    year, month, day = date.split("-")
    hour, minute = time.split(":")

    try:
        event = Event_class.Event_Schedule(name,year,month,day,hour,minute,details)
    
    except:
        return -1

    elist.append(event)
    elist.sort(key=sort_dateToInt)

    return elist.index(event)

def edit(elist, event, name, date, time, details):

    if event not in elist:
        return False
    
    i = elist.index(event)

    year, month, day = date.split("-")
    hour, minute = time.split(":")

    elist[i].event_name = name
    elist[i].date = {"year":year,"month":month,"day":day}
    elist[i].time = {"Hour":hour,"Minutes":minute}
    elist[i].event_detail = details
    elist[i].event_timeleft = elist[i].calculate_time_left()

    elist.sort(key=sort_dateToInt)

    return elist.index(event)

    '''
    try: elist.remove(event)
    except: return False

    i = addEvent(elist, event, name, date, time, details)
    '''

def findTime(elist, keyDate, keyTime):
    """
    elist is a list of events.
    keyDate is a string representing the date. ex: 2022-11-26
    keyTime is a string representing the time.
    It is assumed elist is sorted by date and time. ex: 11:13

    Returns the index of the matching time.

    May build a more efficient binary search if time permits.
    """
    for i in range(len(elist)):
        date = elist[i].get_date()
        time = elist[i].get_time()

        strDate = date[0] + '-' + date[1] + '-' + date[2]
        strTime = time[0] + ':' + time[1]
        if strDate == keyDate and strTime == keyTime:
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

def delete(elist, event):
    '''
    Returns True if event was successfully found and deleted.
    If event wasn't in the list to begin with, returns False.
    '''
    if event in elist:
        elist.remove(event)
        return True
    
    else: return False

#--------------------------------------------------------
# File communication

def dictToEvent(d):
    '''
    Turns a dictionary into an event object.
    Returns the event object.
    '''
    year, month, day = d['Date'].split('-')
    hour, minute = d['Time'].split(':')

    event = Event_class.Event_Schedule(d['Event Name'], year, month, day, hour, \
                                       minute, d['Detail'])

    return event

#--------------------------------------------------------
# Testing
if __name__ == '__main__':
    print(TITLE)

    l = []
    e = l[addEvent(l, "Class", '2022-11-19', '14:20', "Hell in a handbasket")]
    v = l[addEvent(l, "Vacay", '2022-11-21', '12:20', "Cya l8r losers")]
    n = l[addEvent(l, "Board", '2022-11-21', '12:00', "Be early")]
    t = l[addEvent(l, "Wakup", '2022-11-21', '07:30', "Bacon 4 brkfst")]
    
    print()

    print("Testing dateToInt:")
    print(e.dateToInt())

    print()

    '''
    print("Testing comparisons:")
    print(earlier(e, v), equals(e, v), later(e, v))
    print(earlier(v, n), equals(v, n), later(v, n))
    print(earlier(n, t), equals(n, t), later(n, t))
    '''

    print()

    print("Testing addEvent:")
    for i in range(len(l)):
        print(l[i].event_name)
    
    print(sort_dateToInt(e))
    print(sort_dateToInt(t))

    print()

    print("Testing eventToDict")
    diction = e.write_dict()
    print(diction)

    print("Testing dictToEvent")
    diction['name'] = 'Midterm'
    event = dictToEvent(diction)
    print(event.get_event_name(), event.get_date(), event.get_time(), event.get_details())

    '''
    print()

    print("Testing remove:")
    delete(l, n)
    delete(l, e)
    delete(l, n)
    for i in range(len(l)):
        print(l[i].event_name)
    '''
    print()

    print("Testing edit")
    i = edit(l, e, "Class", "2023-11-19", "14:20", "Next sem")
    for i in range(len(l)):
        print(l[i].event_name)
    print(i, '.', l[i].get_event_name(), l[i].get_date(), l[i].get_time(), l[i].get_details())
    print(l.index(e))
