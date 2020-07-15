import os
from controller import pets,rank,food

line = ""
for i in range(0, 53):
    line += '-'


def header():
    # header start
    print(line)
    print('Welcome to Pypet!'.center(53))
    print(line)
# header end
def console():
    os.system('cls')
    # console start
    print(line)
    print('=== RANK LEVEL ==='.center(53))
    print(line)

    for name in rank:
        rank_str = ""
        for rank_item in rank[name]:
            rank_str += str(rank_item) + '|'
        print('| {} |{}'.format(name.ljust(7), rank_str))

    print(line)
    print('~~~ FOOD DETAIL ~~~'.center(53))
    print(line)

    for name in food:
        food_str = ""
        for key, value in food[name].items():
            food_str += str(value).ljust(14) + '|'
        print('| {}|{}'.format(name.ljust(5), food_str))

    print(line)
    print('^^^ CALORIES TYPE ^^^'.center(53))
    print(line)

    calories_type = set()
    for food_code in food:
        calories_type.add(food[food_code]['calories'])
    print(str(sorted(calories_type)).center(50))

    print(line)
    print('>>> RESULT LIST <<<'.center(53))
    print(line)

    for pet in pets:
        print('Hello ' + pet['name'] + '!')
        print(pet['photo'])
        print('Age: ' + str(pet['age']))
        print('Rank: ' + pet['symbol'])
        print('Weight: ' + str(pet['weight']))

        print(line)


    # console end