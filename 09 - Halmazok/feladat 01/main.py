import random
import time
import os
from typing import *

halmaz:List[int]=[]
halmazelemeinekszama:int=None

def hibakiiras(szoveg:str):
    print(szoveg)
    time.sleep(3)
    os.system("cls")

def elemszambekerese()->int:
    eredmeny:int=None
    while eredmeny==None or eredmeny<2:
        data:str=input("Kérem a lista elemeinek számát(min. 2):  ")
        if(data.isnumeric()):
            eredmeny=int(data)
            if(eredmeny<2):
                hibakiiras("legalább 2-t adjon meg")
            else:
                return eredmeny
        else:
            hibakiiras("Nem számot adott meg")

def listakitoltes(lista:List[int], elemekszama:int)->List[int]:
    for i in range(0, elemekszama, 1):
        lista.append(random.randint(0,100))

    return lista

halmazelemeinekszama=elemszambekerese()
halmaz=listakitoltes(halmaz, halmazelemeinekszama)
print(halmaz)