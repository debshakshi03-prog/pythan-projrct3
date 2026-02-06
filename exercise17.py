from datetime import date
from dateutil.relativedelta import relativedelta
def calculate_age():
    try:
        dob_input=input("enter date of birth(dd-mm-yyyy):")
        dob=datetime.strptime(dob_input,"%d-%m-%Y").date()
        today=date.today()
        age=relativedelta(today,dob)
        print(age.years,"year",age.months,"month",age.days,"days")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
calculate_age()

