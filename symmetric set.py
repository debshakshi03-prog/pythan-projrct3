list1 = [101, 102, 103]
list2 = [103, 104, 105]
list3=[]
set1=set(list1)
set2=set(list2)
set3=set1&set2
for x in set1:
    if x not in set3:
        list3.append(x)
for x in set2:
    if x not in set3:
        list3.append(x)
print(set(list3))

