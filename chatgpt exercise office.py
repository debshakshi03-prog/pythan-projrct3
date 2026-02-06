from datetime import datetime
from dateutil.relativedelta import relativedelta
def maintain_office():
    try:
        input_data=input("enter input date(dd/mm/yyyy HH:MM:SS):")
        arrive_time=datetime.strptime(input_data,"%d-%m-%y %H:%M:%S")
        office_time=datetime(arrive_time.year,arrive_time.month,arrive_time.day,9,00,00)
        print(office_time.strftime('%A, %B %d, %Y %I:%M %p'))
        if arrive_time<=office_time:
            print("arrived")
        else:
            diff = arrive_time-office_time
            late_by=diff.seconds//60
            print("late by:",late_by,"mintues")

    except:
        print("error")
maintain_office()

