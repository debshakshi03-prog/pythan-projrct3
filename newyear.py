from datetime import datetime
def calculate_date():
    try:
        now=datetime.now()
        next_year = now.year + 1
        new_year=datetime(next_year,1,1)
        diff=new_year-now
        days=diff.days
        hours=diff.seconds//3600
        minutes=diff.seconds//60
        print(days,hours,minutes)
    except:
        print("error")
calculate_date()
