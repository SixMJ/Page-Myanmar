import dis


def hello_world():
    print('Hello World')


hello_world()

# dis.dis(hello_world)

print('Byte Code')
string = dis.Bytecode(hello_world)
for x in string:
    print(x)
