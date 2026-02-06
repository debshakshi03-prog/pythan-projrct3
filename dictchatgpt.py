students = {
    "Rahim": 45,
    "Karim": 78,
    "Shakshi": 92,
    "Amina": 50,
    "Rafi": 33
}
s={}
for key in students:
    if students[key]>=50:
        s[key]=students[key]
print(s)
