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
    
    def get_modified_date(self):
        monthDays = [29, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        date = self.get_date()
        yr, month, day = int(date[0]), int(date[1]), int(date[2])
        time = self.get_modified_time()
        hour, min = int(time[0]), int(time[1])

        if hour == 23: 
            day -= 1
            if day == 0:
                if yr % 4 == 0: day = monthDays[0]
                else:           day = monthDays[month]
                month -= 1
                if month == 0:
                    month = 12
                    yr -= 1

        yr    = str(yr)
        month = str(month)
        day   = str(day)

        if len(month) == 1: month = "0" + month
        if len(day)   == 1: day   = "0" + day

        return yr,month,day

    def get_details(self):
        return (self.event_detail)
    
    def get_modified_time(self):
        """
        purpose: Modifies the hour time by one hour behind of the set time for the bug feature of our program
        """

        hour = self.time["Hour"]
        min = self.time["Minutes"]
        modified_hour = str(int(hour) - 1)

        if modified_hour == '-1': modified_hour = '23'

        if len(modified_hour) == 1: modified_hour = '0' + modified_hour
        
        return modified_hour,min
    

    def get_time(self):
        hour = self.time["Hour"]
        min = self.time["Minutes"]

        return hour,min

    def calculate_time_left(self):
        """
        Calculates the time left from current time and date, to the date and time of the event
        returns the result in this format: # days, hours:mins:seconds
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


        #In the case the day is passed, return True or else return the result
        for i in str(result):
            if(i=="-"):
                return True

        

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
#     '''
#     ----For Testing purposes--------
#     eventname = Event_Schedule("Birthday","2023","11","20","7","30","None")
#     print(eventname.calculate_time_left())
#     num = eventname.dateToInt()
#     list1 = eventname.write_dict() 
#     print("\n",list1)
#     '''
