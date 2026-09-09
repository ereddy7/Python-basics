from functools import reduce
l=[0,5,10,15,20,25,30]
print(list(filter(lambda x:x%2==0,l)))
print(list(map(lambda x:x*x,l)))
print(reduce(lambda x,y:x+y,l))
