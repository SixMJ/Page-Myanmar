#keyword args cannot declare after required args
def func(name1, message,name2):
    print("printing the message with ",name1,",",message,"and",name2)
func("John",message="hello",name2 = "David")

def func(name1,message,name2):
    print("printing the message with ",name1,",",message,"and",name2)
#func("John",message="hello","David")
