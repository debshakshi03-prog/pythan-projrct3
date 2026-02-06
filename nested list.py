def flatelist(f):
    r=[]
    for item in f:
        if isinstance(item,list):
            r.extend(flatelist(item))
        else:
            r.append(item)
    return r
list1=[1,[2,3,4],5,[6,7]]
result=flatelist(list1)
print(result)