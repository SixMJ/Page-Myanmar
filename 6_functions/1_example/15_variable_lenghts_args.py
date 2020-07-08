def printme(**kwargs):
    print("type of passed argument is ", type(kwargs))
    for key in kwargs:
        print(kwargs[key])
    printme(name = "John", age = 20, weight = 10.5)