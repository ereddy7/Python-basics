word=input("Word:"); found=[]
for ch in word.lower():
    if ch in "aeiou" and ch not in found: found.append(ch)
print(found)
