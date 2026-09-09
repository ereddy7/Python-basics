s=input("Main:"); sub=input("Sub:"); pos=-1; found=False
while True:
    pos=s.find(sub,pos+1)
    if pos==-1: break
    print(pos); found=True
if not found: print("Not Found")
