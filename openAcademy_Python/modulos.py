#Importação de módulos
import math         #Importa todas as funcionalidades da biblioteca 'math'
from math import sqrt, pow #Importa somente a funcionalidade 'sqrt' e 'pow', da biblioteca 'math'
import random
from random import randint
import datetime
from datetime import date, time

def minecraft():
    print(sqrt(25))

minecraft()    

def minecraft():
    print(pow(10, 2))

minecraft()

def GodOfWar():
    for i in range (5):
        print(randint(0, 10))

GodOfWar()

def CallOfDuty():
    print (datetime.datetime(2024, 12, 25, 12, 12, 12))

CallOfDuty()

def CallOfDuty():
    print (time(23, 32, 53))

CallOfDuty()

def CallOfDuty():
    print(f"Date e hora atuais: {datetime.datetime.now()}")

CallOfDuty()

def CallOfDuty():
    print(f"Ano de nascimento: {date(2004, 1, 14)}")

CallOfDuty()