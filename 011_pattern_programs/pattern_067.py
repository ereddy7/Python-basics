# Pattern 67 from the PDF pattern-practice section
# Enter a positive number of rows.
n=int(input("Enter number of rows: "))
for i in range(1,n+1): print(" ".join(str(j) for j in range(n,0,-1)))
