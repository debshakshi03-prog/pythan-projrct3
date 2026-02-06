d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
s={}
all_keys=set(d1.keys())|set(d2.keys())
for key in all_keys:
    values = []
    if key in d1:
        values.append(d1[key])
    if key in d2:
        values.append(d2[key])
    s[key] = values
print(s)