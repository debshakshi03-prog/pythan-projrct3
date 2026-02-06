from itertools import combinations
list1=[1, 2, 3]
power_set=[]
for i in range (len(list1)+1):
    for comb in combinations(list1,i):
        power_set.append(list(comb))
print(power_set)





power_set=sum([list(combinations(list1,i)) for i in range(len(list1)+1)],[])
print(power_set)
