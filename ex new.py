list=["apple", "bat", "cherry", "dog", "elderberry"]
result=[x.upper() for x in list if len(x)>4]
print(result)