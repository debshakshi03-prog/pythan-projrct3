library={"Orwell": ["1984", "Animal Farm"], "Huxley": ["Brave New World"]}
s={}
i=0
for key,value in library.items():
      for i in range(0,len(value)):
          s[value[i]]=key
print(s)