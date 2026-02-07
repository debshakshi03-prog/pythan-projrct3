employees = [
    {"name": "Rahim", "age": 28, "salary": 40000},
    {"name": "Karim", "age": 35, "salary": 55000},
    {"name": "Amina", "age": 22, "salary": 30000},
    {"name": "Salma", "age": 30, "salary": 50000}
]
def stu(s):
    return s["salary"]
    employees.sort(key=stu,reverse=True)
for emp in employees:
    if emp["age"] >=30:
        print(emp["name"],emp["salary"])
