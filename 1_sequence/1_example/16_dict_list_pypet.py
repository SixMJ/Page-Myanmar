cat = {'name':'Garfy' ,
	   'type' : 'cat',
	   'photo':'(=^o.o^=)',
	   'hungry' : True,
	   'weight' : 9.5,
	   'age' : 5
	  }

mouse = {'name':'Fluffy' ,
	   'type' : 'mouse',
	   'photo':'<:3 )~~~',
	   'hungry' : False,
	   'weight' : 1.5,
	   'age' : 6
	  }

fish = {'name':'Nemo' ,
	   'type' : 'fish',
	   'photo':'<`)))><',
	   'hungry' : True,
	   'weight' : 2.1,
	   'age' : 7 
	  }

pets = [cat , mouse , fish]

print(pets)
print('---------------------')
print(pets[0]['name'])
print(pets[0])
print(pets[1]['name'])
print(pets[1])
print(pets[2]['name'])
print(pets[2])