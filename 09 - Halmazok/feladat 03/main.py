import random
import time
import os
from typing import *

halmaz:List[int]=[]
elemszam:int=7
osszeg:int=None
atlag:float=None
hatosokszama:int=None
paratlaokszama:int=None

def listatoltes(elemszama:int)->List[int]:
    randomszam:int=None
    lista:List[int]=[]
    for i in range(0, elemszama, 1):
        randomszam=random.randint(1,6)
        lista.append(randomszam)

    return lista

def listaosszeg(lista:List[int])->int:
    eredmeny:int=0
    for item in lista:
        eredmeny+=item

    return eredmeny

def hatosok(lista:List[int])->int:
    eredmeny:int=0
    for item in lista:
        if item == 6:
            eredmeny+=1

    return eredmeny

def paratlanok(lista:List[int])->int:
    eredmeny:int=0
    for item in lista:
        if item % 2 == 1:
            eredmeny+=1

    return eredmeny

def legtobbetdobottszam(lista:List[int])->Dict[int, int]:
    dobottszamok:Dict[int, int]={
        1: 0,
        2: 0, 
        3: 0,
        4: 0,
        5: 0,
        6: 0
    }
    for item in lista:
        if item==1:
            dobottszamok[1]= dobottszamok[1] + 1
        elif item==2:
            dobottszamok[2]= dobottszamok[2] + 1
        elif item==3:
            dobottszamok[3]= dobottszamok[3] + 1
        elif item==4:
            dobottszamok[4]= dobottszamok[4] + 1
        elif item==5:
            dobottszamok[5]= dobottszamok[5] + 1
        else:
            dobottszamok[6]= dobottszamok[6] + 1

    

halmaz=listatoltes(elemszam)
print(f"a halmaz elemei: {halmaz}")
osszeg=listaosszeg(halmaz)
atlag=osszeg / elemszam
hatosokszama=hatosok(halmaz)
paratlaokszama=paratlanok(halmaz)
print(f"\nA halmaz átlaga: {atlag}\n{hatosokszama} db hatos lett dobva\n{paratlaokszama} db páratlan szám lett dobva.")
listacucc:Dict[int, int]=legtobbetdobottszam(halmaz)
print(listacucc)