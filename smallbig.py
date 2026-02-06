n=input("enter the number:")
m=int(n[0])
m1=int(n[1])
for i in range(len(n)):
    if int(n[i])>m:
        m=int(n[i])
    elif int(n[i])<m:
        m1=int(n[i])
print("maximum num is:",m)
print("minimum num is:",m1)

