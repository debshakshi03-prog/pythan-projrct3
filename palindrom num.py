def  palindrom(sence):
      r=[ch.lower() for ch in sence if ch.isalnum()]
      result="".join(r)
      return result==result[::-1]
print(palindrom("iam shakshi"))


