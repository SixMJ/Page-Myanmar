#call by ref
#defining the function

def change_list(list1):
    list1.append(20)
    list1.append(30)
    print("List inside function = ",list1)

#defining the list
list1 = [10,30,40,50]

#calling the function
change_list(list1)
print("List outside function = ",list1)
