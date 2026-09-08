fs=frozenset({10,20,30,40})
print(fs,type(fs))

#frozenset({40, 10, 20, 30}) <class 'frozenset'>

fs.add(20)

#     fs.add(20) AttributeError: 'frozenset' object has no attribute 'add'