x=[10,20,20,30]
print(x)
print(len(x),x.count(20),x.index(20))
x.append(40); 
print(x)
x.insert(1,15); 
print(x)
x.extend([50,60]); 
print(x)
x.remove(20); 
print(x)
print(x.pop()); 
print(x)
x.reverse(); 
print(x)
x.sort(); 
print(x)


#[10, 20, 20, 30]
#4 2 1
#[10, 20, 20, 30, 40]
#[10, 15, 20, 20, 30, 40]
#[10, 15, 20, 20, 30, 40, 50, 60]
#[10, 15, 20, 30, 40, 50, 60]
#60
#[10, 15, 20, 30, 40, 50]
#[50, 40, 30, 20, 15, 10]
#[10, 15, 20, 30, 40, 50]