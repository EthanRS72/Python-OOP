import re

class Date:
    dates = []

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        Date.dates.append(self)

    #Instance method requires self.
    def format_date(self):
        return str(self.day) + "/" + str(self.month) + "/" + str(self.year)
    
    @classmethod
    def date_from_string(cls, string):
        #Returns a list, use [0] to get first date passed
        date = re.findall('\d{2}-\d{2}-\d{4}|\d{2}/\d{2}/\d{4}', string)[0]
        date_list = date.replace("-", "/").split("/")
        day = date_list[0]
        month = date_list[1]
        year = date_list[2]
        #Ensure same order as contructor (__init__)
        return cls(year, month, day)

    @staticmethod #Static method uses less memory, does not require access to the object or class
    #YYYY/MM/DD -> DD/MM/YYYY
    def YMD_to_DMY(string):
        lst = string.replace("-", "/").split("/")
        return lst[2] + "/" + lst[1] + "/" + lst[0]

d1 = Date(2022, 6, 17)

print(d1.__dict__)
print(d1.format_date())

d2 = Date.date_from_string("Today's date is 15-04-2021")

print(d2.__dict__)
print(d2.format_date())

d3 = Date.YMD_to_DMY("2020-02-10")
print(d3)