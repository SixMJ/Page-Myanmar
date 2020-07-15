import pickle
from os import path
from model import pets,rank,food,pettype


def dashboard():
    sr = 0
    print('Please select pypet ...')
    for pet in pets:
        print('(' + str(sr+1) + ') ' + str(pet['name']))
        sr += 1
    pet_no = int(input())
    pet_no = pet_no - 1

    return pet_no


def save(**kwargs):
    for kw in kwargs:
        values = kwargs[kw]
        file_name = kw + "_data.txt"
        file = open(file_name, 'wb')
        pickle.dump(values, file)
        file.close()


def read(**kwargs):
    for kw in kwargs:
        file_name = kw + "_data.txt"
        file = open(file_name, 'rb')
        data = pickle.load(file)
        file.close()
        return data


def create():
    new_rank = []
    new_rank_name = input('New Rank Name : ')
    new_rank_symbol = input('New Rank Symbol : ')
    for level in range(0, 4):
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
    pettype.append(new_pet_type)

    new_pet = {}
    new_pet["name"] = input("New Pet Name : ")
    new_pet["type"] = new_pet_type
    new_pet["age"] = int(input("New Pet Age: "))
    new_pet["level"] = int(input("New Pet Level: "))
    new_pet["weight"] = float(input("New Pet Weight: "))
    new_pet["hungry"] = bool(input("New Pet Hungry: "))
    new_pet["photo"] = input("New Pet Photo: ")
    new_pet["symbol"] = rank[new_rank_name][new_pet["level"]][1]
    new_pet["food"] = food[new_food_code]
    pets.append(new_pet)


def delete(pet_no):
    delete_rank = pets[pet_no]['rank']
    food_name = str(pets[pet_no]['food']['name'])
    delete_food = str('v' + food_name[-1:]).lower()

    del rank[delete_rank]
    del food[delete_food]
    del pets[pet_no]


def feed(pet):

    # feed start
    if pet['hungry'] and pet['level'] < 1:
        print(pet['name'] + ' is hungry!')
    elif pet['hungry'] and pet['level'] > 0:
        print(pet['name'] + ' is hungry!')
        print(pet['name'] + ' need food!')

        # get amount, calories
        ams = pet['food']['amount']
        amount = float(ams[:ams.find('k')])
        cals = pet['food']['calories']
        calories = float(cals[:cals.find('c')])
        ####

        level = pet['level']
        pet['weight'] += ((calories * amount) * level)

        print('Amount : ' + str(amount) + ' kg')
        print('Calories : ' + str(calories) + ' cal')
        print('Current Weight: ' + str(pet['weight']))
    else:
        print(pet['name'] + ' is not hungry!')
        # feed end