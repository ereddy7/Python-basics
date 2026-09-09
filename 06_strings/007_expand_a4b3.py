s=input("Pattern:"); out=""; previous=""
for x in s:
    if x.isalpha(): previous=x; out+=x
    else: out+=previous*(int(x)-1)
print(out)
