import os
import sys
from view import header, console
from controller import dashboard, save, create, delete, feed
from controller import pets, rank, food, pettype


def main():
    print('Please select your operation ...')
    print('(1) Create Pypet')
    print('(2) Update Pypet')
    print('(3) Delete Pypet')
    print('(4) Feedto Pypet')
    print('(5) Exit!')
    select = int(input())

    if select is 5:
        os.system('cls')
        sys.exit()
    elif select is 4:
        pet_no = dashboard()
        pet = pets[pet_no]
        feed(pet)
    elif select is 3:
        pet_no = dashboard()
        delete(pet_no)
    elif select is 2:
        pet_no = dashboard()
        delete(pet_no)
        create()
    elif select is 1:
        n = int(input("Total Pet : "))
        while n > 0:
            n -= 1
            create()

    console()
    save(pets=pets, pettype=pettype, rank=rank, food=food)
    main()


main()
