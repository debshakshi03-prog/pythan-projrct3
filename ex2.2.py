dict1={"a":1,"b":2,"c":3,"d":4}
dict2={"a":1,"e":2,"f":3,"g":4}
result={}
for key in dict1:
    result[key]=dict1[key]+dict2.get(key,0)
for key in dict2:
    if key not in result:
        result[key]=dict2[key]
print(result)