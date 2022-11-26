#This is the event_Schedule class created by Ayub

class Event_Schedule():

    def __init__(self,name,year,month,day,hour,minute,details):
        """
        The contructor
        purpose: Create a Event instance
        """
        self.event_name= name
        self.date = {"year":year,"month":month,"day":day}
        self.time = {"Hour":hour,"Minutes":minute}
        self.event_detail = details
        self.event_timeleft = self.calculate_time_left()
       
    def get_event_name(self):
        return(self.event_name)

    def get_date(self):
        yr = self.date["year"]
        mon = self.date["month"]
        day = self.date["day"]
        return yr,mon,day

    def get_details(self):
        return (self.event_detail)
    
    def get_time(self):
        hour = self.time["Hour"]
        min = self.time["Minutes"]

        return hour,min

    def calculate_time_left(self):
        """
        Calculates the time left from current time and date, to the date and time of the event
        """
        import datetime
        today = datetime.date.today()
        timenow = datetime.datetime.now()
        yr,mon,day = self.get_date()
        hr,min = self.get_time()
        temp = "{}-{}-{} {}:{}".format(yr,mon,day,hr,min)
        deadline = str(temp)
        current_time = str(today) + " " + str(timenow.strftime("%H:%M"))
        start_date = datetime.datetime.strptime(current_time,'%Y-%m-%d %H:%M')
        end_date = datetime.datetime.strptime(deadline, '%Y-%m-%d %H:%M')
        result = end_date-start_date
        return result

    def dateToInt(self):

        """
        returns an integer with the year, month, day, hour, and minute.
        Ex. Nov 19, 2022 12:33pm becomes: 202211191233
        Used for date and time comparison.
        Contributed by Brant
        """
        date = self.get_date()
        time = self.get_time()

        integer =  date[0] + date[1] + date[2] 
        integer += time[0] + time[1]

        return int(integer)

    def write_dict(self):

        #Formats the data into strings
        yr,mon,day = self.get_date()
        hr,min = self.get_time()
        event_name = "{}".format(self.event_name)
        date = "{}-{}-{}".format(yr,mon,day)
        time = "{}:{}".format(hr,min)
        detail = "{}".format(self.event_detail)

        #dictionary format
        event_dict = {"Event Name":event_name,"Date":date,"Time":time,"Detail":detail}
        return event_dict

    
  
# if __name__ == "__main__":
#     eventname = Event_Schedule("Birthday","2023","11","15","7","30","None")
#     num = eventname.dateToInt()
#     list1 = eventname.write_dict() 
#     print(list1)
