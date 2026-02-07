from datetime import date
from dateutil.relativedelta import relativedelta
import calendar
def calculate_age():
    dob_input=input("Enter your date of birth(YYYY-MM-DD): ")
    dob=date.fromisoformat(dob_input)
    today=date.today()
    age=relativedelta(today,dob)
    print(age.years,age)
    print(calendar.month_name[dob.month])
calculate_age()




