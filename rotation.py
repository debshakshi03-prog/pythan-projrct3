def rotataion(list,n,direction):
     if not list:
         return list
     n=n%len(list)
     if direction=="left":
        return list[n:]+list[:n]
     else:
       return list[-n:]+list[:-n]
list=[1,2,3,4,5,6,7]
print(rotataion(list,3,"right"))
