# dashboard -> pet_no = dashboard
# delete    -> delete(pet_no)
# create    -> create()

line = ""
for i in range(0,54):
	line += '-'

print(line)
print('Welcome to Pypet!' .center(53))
print(line)

########### ENTITY (MODEL) #########

rank = {
	'star' : [(0,'✶'), (1,'✶✶'), (2,'✶✶✶'),(3,'✶✶✶✶')],
	'circle' : [(0,'●'), (1,'●●'), (2,'●●●'),(3,'●●●●')],
	'heart' : [(0,'♥'), (1,'♥♥'), (2,'♥♥♥'),(3,'♥♥♥♥')],
	
}
food = {
	'va': {
	'name': 'Vitamin-A',
	'calories' : '4cal',
	'amount'   : '1kg'
	},
	'vb': {
	'name': 'Vitamin-B',
	'calories' : '2cal',
	'amount'   : '1.5kg'
	},
	'vc': {
	'name': 'Vitamin-C',
	'calories' : '1cal',
	'amount'   : '1kg'
	}
}

pettype = ['cat','mouse','fish']

cat = {
'name':'Garfy',
'type' : pettype[0], 
'age' : 5, 
'rank' : 'star',
'symbol' : rank ['star'] [2][1],
'level' : rank ['star'][2][0],
'food' :food['va'],
'weight' : 9.5 , 
'hungry' : True , 
'photo' : '(=^o.o^=)__'
}

mouse = {
'name' : 'Fluffy',
'type' : pettype[1],
'age' : 6,
'rank' : 'circle',
'symbol' : rank ['circle'] [1][1],
'level' : rank ['circle'][1][0],
'food' :food['vb'],
'weight':1.5,
'hungry' : True,
'photo' : '<:3 )~~~~'
}

fish = {
'name' :'Nemo',
'type' : pettype[2],
'age' : 7,
'rank' : 'heart',
'symbol' : rank ['heart'] [0][1],
'level' : rank ['heart'][0][0],
'food' :food['vc'],
'weight' : 2.1,
'hungry' : True,
'photo' : '<`)))><'
}

pets = [cat, mouse, fish]

########### INPUT (CTRL) #########
def dashboard():
    pass

def create():
    pass

def delete(pet_no):
    pass

print('Please select your operation...')
print('(1) Create Pyoet')
print('(2) Update Pypet')
print('(3) Delect Pypet')
select = int(input())

if select is 3:

	#dashbord start
	 pet_no = dashboard
	#dashbord end

	#delete start
	delete(pet_no)
	#delete end
	

elif select is 2:

	#When select is 2

	#update dashboard start
	pet_no = dashboard
	#update dashboard end

	#update delete start
	delete(pet_no)
	#update delete end

	#update create start
	crete()
	#update create end

elif select is 1:
	n = int(input("Total Pet: "))

	while n > 0:
		n -= 1

		#create start
		new_rank = []
		new_rank_name = input('New Rank Name : ')
		new_rank_symbol = input('New Rank Symbol : ')
		for level in range(0,4):
			new_rank.append(tuple([level, new_rank_symbol * (level + 1)]))
		else:
			rank.update({new_rank_name: new_rank})

		new_food = {}
		new_food_code = input("New Food Code: ")
		new_food_name = input("New Food Name: ")
		new_food["name"] = new_food_name
		cal = input("New Food Calories: ")
		new_food["calories"] = cal + 'cal'
		amount = input("New Food Amount: ")
		new_food["amount"] = amount + 'kg'
		food.update({new_food_code: new_food})

		new_pet_type = input("New Pet Type Name: ")
		pettype.append({new_pet_type})
		
		new_pet = {}
		new_pet["name"] = input("New Pet Name : ")
		new_pet["type"] = new_pet_type
		new_pet["age"] = int(input("New Pet Age : "))
		new_pet["level"] = int(input("New Pet Level : "))
		new_pet["weight"] = float(input("New Pet Weight : "))
		new_pet["hungry"] = bool(input("New Pet Hungry : "))
		new_pet["photo"] = input("New Pet Photo : ")
		new_pet["symbol"] = rank[new_rank_name][new_pet["level"]][1]
		new_pet["food"] = food[new_food_code]
		pets.append(new_pet)
		#create end
########### PRINT (VIEW) #########

print('=== RANK LEVEL ==='. center(53))
print(line)

for name in rank:
	rank_str = ""
	for rank_item in rank[name]:
		rank_str += str(rank_item) + '|'
	print('| {} | {}'.format(name.ljust(7),rank_str))

print(line)
print('~~~ FOOD DETAIL ~~~'.center(53))
print(line)

for name in food:
	food_str = ""
	for key,value in food[name].items():
		food_str += str(value).ljust(14) + '|'
	print('| {}|{}'.format(name.ljust(5),food_str))

print(line)
print('~~~ CALORIES TYPE ~~~'.center(53))
print(line)

calories_type = set()
for food_code in food:
	calories_type.add(food[food_code]['calories'])
print(str(sorted(calories_type)).center(50))

print(line)
print('>>> RESULT LIST <<<'.center(53))
print(line)

for pet in pets:

	print ('Hello ' + pet['name'] + '!')
	print (pet['photo'])
	print (pet['type'])
	print ('Age: ' + str(pet['age']))
	print('Rank: ' + pet['symbol'])
	print ('Weight: '+ str(pet['weight']))
	if pet['hungry'] and pet['level'] < 1:
		print(pet['name'] + ' is hungry!')
	elif pet['hungry'] and pet['level'] > 0:
		print(pet['name'] + ' is hungry!')
		print(pet['name'] + ' need food!')
		print('Food contains ' + pet ['food']['calories'])
		ams = pet['food']['amount']
		amount = float(ams[:ams.find('k')])
		cals = pet['food']['calories']
		calories = float(cals[:cals.find('c')])
		level = pet['level']
		pet['weight'] += ((calories * amount) * level)
		print('Amount : ' + str(amount) + ' kg')
		print('Calories : ' + str(calories) + ' cal')
		print('Current Weight:' + str(pet['weight']))
	else:
		print(pet['name'] + ' is not hungry!')
	print (line)

	#When select is 2

	#update dashboard start
	#update dashboard end

	#update delete start
	#update delete end

	#update create start
	#update create end

    # dashboard -> pet_no = dashboard
    # delete    -> delete(pet_no)
    # create    -> create()