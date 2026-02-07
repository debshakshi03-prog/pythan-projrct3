students = [
    {"name": "Rahim", "marks": 75},
    {"name": "Karim", "marks": 45},
    {"name": "Amina", "marks": 90},
    {"name": "Salma", "marks": 60}
]
def stu(s):
    return s["marks"]
students.sort(key=stu,reverse=True)
for student in students:
    print(student["name"])
