text=["apple", "education", "ice", "ocean", "python", "umbrella"]
r=[x for x in text if len(x)>5 and x[0] in 'aeiou']
print(r)