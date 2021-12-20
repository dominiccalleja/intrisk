
"""
This script contains a class for the management of incident data
"""



class Incident():
    incident_severity = 1   # You can allocate self variables without the self. when you do it before the __init__
    __verbose__ = True # I always lik to have a __verbose__ variable in every class. When a variable has '__' at the begining and end that variable is private and only accessed from within the class 

    def __init__(self, incident_id, date, time, location):
        self.incident_id = incident_id
        self.date = date
        self.time = time
        self.location = location
       
    def get_date(self):
        "Function to return the incident date"
        return self.date

    def get_time(self):
        "Function to return the "
        return self.time

    def get_incident_severity(self):
        return self.incident_severity

    def gen_label(self):
        label = '{}-{}{}-({})'.format(self.incident_id,self.date,self.time,self.location)
        if self.__verbose__:  # This is an example of how to build your print statements. print statements are great to help you when running the code. But they can be annoying when you run the code in production so its a good idea to always use this structure
            print(label)
            
def print_incident(A):
    return A

