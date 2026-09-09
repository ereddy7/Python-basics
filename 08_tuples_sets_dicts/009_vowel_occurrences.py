word=input("Word:").lower(); d={}
for x in word:
    if x in "aeiou": d[x]=d.get(x,0)+1
for k,v in sorted(d.items()): print(k,v)
