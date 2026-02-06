list1=input("Enter a list:").split(",")
list2=input("Enter another list:").split(",")
set1=set(list1)
set2=set(list2)
if set1.issubset(set2):
    print("set1 is subset of set2")
elif set1.issuperset(set2):
    print("set1 is superset of set2")
elif set1.isdisjoint(set2):
    print("set1 is disjoint of set2")
else:
    print("no special relation")

