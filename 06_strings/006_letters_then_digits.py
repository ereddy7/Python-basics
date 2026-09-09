s=input("String:")
letters=sorted(x for x in s if x.isalpha())
digits=sorted(x for x in s if x.isdigit())
print("".join(letters+digits))
