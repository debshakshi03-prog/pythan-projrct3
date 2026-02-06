def merge(dict1, dict2):
    r=dict1.copy()
    for key,value in dict2.items():
      r[key] =r.get(key,0) + value
    return r
d1={"a":1,"b":2,"c":3}
d2={"a":4,"e":5,"f":6}
print(merge(d1,d2))