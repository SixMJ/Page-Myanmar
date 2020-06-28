line = ""
for i in range (0 , 53):
  line += '-'

print(line)
print('Welcome to Pypet!')
print(line)

rank = {
  'star': [(0,'✰'),(1,'✰✰'),(2,'✰✰✰'),(3,'✰✰✰✰')],
  'circle': [(0,'ꔷ'),(1,'ꔷꔷ'),(2,'ꔷꔷꔷ'),(3,'ꔷꔷꔷꔷ')],
  'heart': [(0,'♥'),(1,'♥♥'),(2,'♥♥♥'),(3,'♥♥♥♥')]
}

food = {
  'va': {
    'name': 'Vitamin-A',
    'calories' : '4cal',
    'amount': '1kg'
  },
  'vb': {
    'name': 'Vitamin-B',
    'calories' : '2cal',
    'amount': '1.5kg'
  },
  'vc': {
    'name': 'Vitamin-C',
    'calories' : '1cal',
    'amount': '1.5kg'
  }
}

cat = {
  'name': 'Garfy',
  'type': 'cat',
  'hungry': True,
  'weight': 9.5,
  'age': 5,
  'level': rank['star'][2][0],
  'symbol': rank['star'][2][1],
  'food': food['va'],
  'photo': '(=^o.o^=)__',
}

mouse = {
  'name': 'Fluffy',
  'type': 'mouse',
  'age': 6,
  'weight': 1.5,
  'hungry': True,
  'level': rank['circle'][1][0],
  'symbol': rank['circle'][1][1],
  'food': food['vb'],
  'photo': '<:3 )~~~~',
}

fish = {
  'name': 'Nemo',
  'type': 'fish',
  'age': 7,
  'weight': 2.1,
  'hungry': True,
  'level': rank['heart'][0][0],
  'symbol': rank['heart'][0][1],
  'food': food['vc'],
  'photo': '<`)))><',
}

pets = [cat, mouse, fish]

for pet in pets:

  print('Hello ' + pet['name'] + '!')
  print(pet['photo'])
  print('Age: ' + str(pet['age']))
  print('Rank: ' + pet['symbol'])
  print('Weight: ' + str(pet['weight']))
  if pet['hungry'] and pet['level'] < 1:
    print(pet['name'] + ' is hungry!')
  elif pet['hungry'] and pet['level'] > 0:
    print(pet['name'] + ' is hungry!')
    print(pet['name'] + ' need food!')

    ams = pet['food']['amount']
    amount = float(ams[:ams.find('k')])
    cals = pet['food']['calories']
    calories = float(cals[:cals.find('c')])
    level = pet['level']
    pet['weight'] += ((calories * amount ) * level) 
    print('Amount : ' + str(amount) + ' kg')
    print('Calories : ' + str(calories) + ' cal')
    print('Current Weight: ' + str(pet['weight']))
  else:
    print(pet['name'] + ' is not hungry!')
  print(line)


