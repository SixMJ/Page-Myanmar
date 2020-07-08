def printme(*names):
    print("type of passed argument is ",type(names))
    for name in names:
        print(name)
printme("John", "David", "Smith", "Nick")