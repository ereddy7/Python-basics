eno=int(input("Employee No:"))
ename=input("Employee Name:")
esal=float(input("Employee Salary:"))
eaddr=input("Employee Address:")
married=input("Married [True|False]:").strip().lower()=="true"
print(eno,ename,esal,eaddr,married)
