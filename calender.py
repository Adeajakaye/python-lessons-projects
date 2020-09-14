import calendar

import datetime

c=calendar.TextCalendar(calendar.SUNDAY)
date=c.formatmonth(2020,2,2)
    
print(date)
    
yy=int(input("please enter the year: "))
mm=int(input("please enter the month: "))
dd=int(input("please enter the day: "))
    
print(date)

Today=datetime.datetime.now()
Today_date=Today.strftime("%B-%d-%Y")
print(Today)
print(Today_date)
y = str("February-14-2020")

if Today_date == y:
        print("Today is valentine, hope you had a nice day with your lover")
else:
    print("valentine is gone, now you will be lonely again")  