employees = [{"name": "A", "salary": 50}, {"name": "B", "salary": 70}, {"name": "C", "salary": 60}]
employees.sort(key=lambda x: x["salary"],reverse=True)
for emp in employees:
    print(emp["name"],emp["salary"])
