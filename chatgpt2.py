def notvowl(s):
    se=s.lower()
    r=[ch for ch in se if ch not in 'aeiou']
    return ("".join(r))
print(notvowl("shakshi"))
