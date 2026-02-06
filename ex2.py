list=[]
for i in range(6):
    n=int(input("Enter  the number:"))
    list.append(n)
print(list)
for i in list:
    if i%5==0 :
        print(i)
    elif i<150:
        continue
    elif i>500:
        break
