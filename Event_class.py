#This is the event_Schedule class created by Ayub

class Event_Schedule():

    def __init__(self,name,year,month,day,hour,minute,start_time,end_time,details):
        """
        The contructor
        purpose: Create a Event instance
        """
        self.event_name= name
        self.date = {"year":year,"month":month,"day":day}
        self.time = {"Hour":hour,"Minutes":minute}
        self.event_detail = details
        self.event_timeleft = self.calculate_time_left()
        self.starttime = start_time
        self.endtime = end_time
        
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
        h = self.time["Hour"]
        m = self.time["Minutes"]

        return h,m

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
        Passed an Event_Schedule obj and returns an integer
        with the year, month, day, hour, and minute.
        Ex. Nov 19, 2022 12:33pm becomes: 202211191233
        Used for date and time comparison.
        """
        date = self.get_date()
        time = self.get_time()

        integer =  date[0] * 100000000 + date[1] * 1000000 + date[2] * 10000
        integer += time[0] * 100 + time[1]

        return integer

    def write_dict(self):
        yr,mon,day = self.get_date()
        hr,min = self.get_time()
        event_name = "{}".format(self.event_name)
        date = "{}-{}-{}".format(yr,mon,day)
        time = "\nEvent Time: {}:{}".format(hr,min)
        start_time = "\n Start Event: {}:{}".format(hr,min)
        end_time = "\n End Event: {}:{}".format(hr,min)
        time_left = "\nTime Left before Event starts: {}".format(self.event_timeleft)
        detail = "\nDetail: {}\n".format(self.event_detail)

        #dictionary format
        event_dict = {"Event Name":event_name,"Date":date,"Time":time,"Start Time":start_time,"End Time":end_time,"Time Left":time_left,"Detail":detail}

        return event_dict

    
  
