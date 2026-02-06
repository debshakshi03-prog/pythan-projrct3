from collections import Counter
def frequency(s):
      clean=s.lower().replace(" ","")
      c=Counter(clean)
      return c
s=input("enter string:")
result=frequency(s)
print(result)
