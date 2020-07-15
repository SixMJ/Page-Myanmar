rank = {
    'star': [(0, '✰'), (1, '✰✰'), (2, '✰✰✰'), (3, '✰✰✰✰')],
    'circle': [(0, 'ꔷ'), (1, 'ꔷꔷ'), (2, 'ꔷꔷꔷ'), (3, 'ꔷꔷꔷꔷ')],
    'heart': [(0, '♥'), (1, '♥♥'), (2, '♥♥♥'), (3, '♥♥♥♥')]
}

food = {
    'va': {
        'name': 'Vitamin-A',
        'calories': '4cal',
        'amount': '2kg'
    },
    'vb': {
        'name': 'Vitamin-B',
        'calories': '2cal',
        'amount': '1.5kg'
    },
    'vc': {
        'name': 'Vitamin-C',
        'calories': '1cal',
        'amount': '1kg'
    }
}

pettype = ['cat', 'mouse', 'fish']

cat = {
    'name': 'Garfy',
    'type': pettype[0],
    'hungry': True,
    'weight': 9.5,
    'age': 5,
    'rank': 'star',
    'level': rank['star'][2][0],
    'symbol': rank['star'][2][1],
    'food': food['va'],
    'photo': '(=^o.o^=)__',
}

mouse = {
    'name': 'Fluffy',
    'type': pettype[1],
    'age': 6,
    'weight': 1.5,
    'hungry': True,
    'rank': 'circle',
    'level': rank['circle'][1][0],
    'symbol': rank['circle'][1][1],
    'food': food['vb'],
    'photo': '<:3 )~~~~',
}

fish = {
    'name': 'Nemo',
    'type': pettype[2],
    'age': 7,
    'weight': 2.1,
    'hungry': True,
    'rank': 'heart',
    'level': rank['heart'][0][0],
    'symbol': rank['heart'][0][1],
    'food': food['vc'],
    'photo': '<`)))><',
}

pets = [cat, mouse, fish]