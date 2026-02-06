from datetime import datetime,timedelta,date
def different_date(end):
    today=datetime.today().date()
    current_date=today
    count=0
    while current_date<=end:
        current_date=current_date+timedelta(days=1)
        count=count+1
    return count
end=input("enter the end date(dd/mm/yyyy): ")
end=datetime.strptime(end,"%d/%m/%Y").date()
print(end.strftime('%A, %m/%d/%Y'))
print(different_date(end))