def outer():
    def inner(): print("inner function")
    return inner
f=outer(); f()
