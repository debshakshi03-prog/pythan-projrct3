text=("pythan is easy and pythan is powerful")
t=text.split()
s=[]
list=[]
for i in t:
    if i not in s:
        s.append(i)
        list.append(i)
l=" ".join(list)
print(l)