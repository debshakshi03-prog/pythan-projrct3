def orderd(item):
    seen=set()
    list=[]
    for x in item:
        if x not in seen:
            list.append(x)
            seen.add(x)
    return list
print(orderd([1,2,1,3,1]))