a=input("First:"); 
b=input("Second:")
out=""
for i in range(max(len(a),len(b))):
    if i<len(a): out+=a[i]
    if i<len(b): out+=b[i]
print(out)

