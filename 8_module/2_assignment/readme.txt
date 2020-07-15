model.py	->entity
view.py		->header,console
controller.py   ->dashboard,save,create,read,delete,feed
main.py

view.py
--------
import os
from controller import pets,rank,food

controller.py
--------------
import pickle
from os import path
from model import pets,rank,food,pettype

main.py
--------
import os
import sys
from view import header,console
from comtroller import dashboard,save,create,delete,feed
from contoller import pets,rank,food,pettype
