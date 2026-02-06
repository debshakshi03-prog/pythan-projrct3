def anargram(s1,s2):
    str1=sorted(s1.lower().replace(" ",""))
    str2=sorted(s2.lower().replace(" ",""))
    return  str1==str2
w1,w2=input().split()
result=anargram(w1,w2)
print(result)