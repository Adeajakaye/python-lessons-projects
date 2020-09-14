import datetime
from datetime import datetime
from datetime import timedelta



import calendar
c = calendar.TextCalendar(calendar.SUNDAY)
date= c.formatmonth(2020,1)
print(date)


Today = datetime.now()
Today_date =Today.strftime( "%A %d, %B, %Y")
month =Today.strftime("%B")
print(month)
day= Today.strftime("%A")
print(day)
print(Today_date)
print(Today.month)
print(Today.day)


#adding 30 days

print(Today + timedelta(days=30))


#adding 28 days
print(Today + timedelta(days=28))

# pd means Period date
# ND means new date
# MYPD means my period date

pd=input("is today the last day of your period? Enter Y if yes or enter N if no: ")
if pd == "Y":
    print(Today_date)
    new_date = Today + timedelta(days=28)
    new_date2 = Today + timedelta(days=30)  

    new_date3= new_date.strftime("%A %d, %B, %Y")
    new_date4= new_date2.strftime("%A %d, %B, %Y")


    ND = "This is your next period date : " + str(new_date3) 
    print(ND)

    ND2 ="It maybe two days late(depending on your cycle) which is: " +str(new_date4)
    print(ND2)


elif pd == "N":
    date_entry =input("enter a date:(format- yy,mm,dd) ")
    day, month, year= map(int, date_entry.split(","))
    date7=datetime(day, month, year)
    print(date_entry)
    print(date7.strftime("%Y, %B, %A %d"))

    my_date2= date7 + timedelta(days=28)
    my_date3= date7 + timedelta(days=30)

    my_date5= my_date2.strftime("%Y, %B, %A %d")
    my_date6= my_date3.strftime("%Y, %B, %A %d")

    

    ND3 = "This is your next period date: " + str(my_date5)
    ND4= "It maybe two days late(depending on your cycle) which is: " + str(my_date6)

    print(ND3)
    print(ND4)
    
else:
    print("you entered a wrong input")



import datetime
import os
import vlc


p=vlc.MediaPlayer("11 He's Able.mp3")
stop = False
while stop == False:
    alarm = new_date3
    print(alarm)
    if alarm >= new_date3:
        stop = True
        os.system("start ta lo so pe.mp3")
    







    




