from datetime import date
from dateutil.relativedelta import relativedelta
def calculate_age():
    dob_input=input("enter date of birth(yyyy-mm-dd):")
    dob=date.fromisoformat(dob_input)
    today=date.today()
    age=relativedelta(today,dob)
    print(age.years,"year",age.months,"month",age.days,"days")
calculate_age()