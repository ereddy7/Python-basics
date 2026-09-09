def fact(n):
    result=1
    while n>=1: result*=n; n-=1
    return result
for i in range(1,5): print(i,fact(i))
