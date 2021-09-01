#This is where we used python calendar to display the date and month
#Convert year and date in int

import calendar
date_str=int(input("Enter the Date"))
Year=int(input("Enter the Year"))
print(calendar.month(Year, date_str))