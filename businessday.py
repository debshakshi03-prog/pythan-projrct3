from datetime import date,timedelta,datetime
def officedays(start_day,n):
    current_date = start_day
    count = 0
    while count <n:
        current_date = current_date + timedelta(days=1)
        if current_date.weekday() <5:
            count += 1
    return current_date
start_day = datetime(2026,1,2)
result = officedays(start_day,6)
print(result.strftime('%A, %Y-%m-%d'))
print(f"Start: {start_day.strftime('%A, %Y-%m-%d')}")




