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
	   'age' : 7 ,
	  }

pets = [cat , mouse , fish]

print("Welcome To Pypet!")
print('---------------------')
print('Hello ' + pets[0]['name'])
print(pets[0]['photo'])
print(pets[0][str('age')])
print(pets[0][str('weight')])

print('---------------------')
print('Hello ' + pets[1]['name'])
print(pets[1]['photo'])
print(pets[1][str('age')])
print(pets[1][str('weight')])

print('---------------------')
print('Hello ' + pets[2]['name'])
print(pets[2]['photo'])
print(pets[2][str('age')])
print(pets[2][str('weight')])