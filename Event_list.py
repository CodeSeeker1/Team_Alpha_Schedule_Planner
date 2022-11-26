TITLE = "Event_list.py 1.07 2022-11-26"
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
    "Returns the datToInt of event."
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

#---------------------------------------------------------
def errorChecking(name, date, time):
    '''
    Ensures that the parameters given are in proper format.

    Used internally for addEvent.

    Returns 1 if no errors are found.
    Returns -2 if there is an error in name.
    Returns -3 if there is an error in time.
    '''

    for c in name:
        if c != ' ': break
        return -2
    
    if name == "": return -2
    
    if ':' not in time:
        return -3
    
    hour, minute = time.split(":")

    if (not(hour.isnumeric() and minute.isnumeric() and len(hour) == 2 and len(minute) ==2)):
        return -3

    return 1

#---------------------------------------------------------
# Adding, searching, deleting and editing
def addEvent(elist, name, date, time, details):
    """
    elist is a list of events. 
    Other parameters correspond to the parameters of an Event_Schedule object. 
    Will add error checking for each parameter!

    Adds event object to list and sorts it based on date and time.
    returns index of event object.
    
    Returns a negative number if an error occurs:
    -1: Event Creation failed
    -2: name is empty
    -3: time is in a bad format
    """
    error = errorChecking(name, date, time)
    if error != 1: return error

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
    '''
    Takes a list, event, and event parameters.
    Modifies the values in event to be in line with name, date, time, details.
    Sorts the list afterwards.

    Returns new index of event.
    Returns -1 if event is not in the list.
    '''

    if event not in elist:
        return -1
    
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

def delete(elist, event):
    '''
    Returns True if event was successfully found and deleted.
    If event wasn't in the list to begin with, returns False.
    '''
    if event in elist:
        elist.remove(event)
        return True
    
    else: return False

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

#---------------------------------------------------------
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

'''
def dictToEvent_List(dL):
    
    dl is a list of dictionaries.

    Creates a list of events out of a list of dictionaries.

    Returns the list of events.
    
    l = []
    
    for d in dL:
'''    

#---------------------------------------------------------
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

    print()

    print("Testing error checking:")
    print(addEvent(l, " ", "2022-11-26", "16:26", "Hey"))
    print(addEvent(l, "",  "2022-11-26", "16:26", "Hey"))
    print(addEvent(l, "Test",  "2022-11-26", "16 26", "Hey"))
    print(addEvent(l, "Test",  "2022-11-26", "4:26", "Hey"))