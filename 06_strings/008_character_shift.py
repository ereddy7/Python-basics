s=input("Pattern:"); out=""; previous=""
for x in s:
    if x.isalpha(): previous=x; out+=x
    else: out+=chr(ord(previous)+int(x))
print(out)
