dict = { 'list1': [1,9,8] , 'list2': [1,3,5] }

for index in dict:
	not_contain = True
	for i in dict[index]:
		if i%2 == 0 :
			print (index + " contain an even number!")
			break
else:
	print (index + " does not contain an even number!")