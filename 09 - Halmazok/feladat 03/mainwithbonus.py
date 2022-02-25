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
legtobbetdobott:int=None

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
        if (item % 2 == 1):
            eredmeny+=1

    return eredmeny

#bonusz

def dobottszamokszama(lista:List[int])->Dict[int, int]:
    dobottszamok:Dict[int, int]={
        1: 0,
        2: 0, 
        3: 0,
        4: 0,
        5: 0,
        6: 0
    }
    for item in lista:
        for i in range(1, len(dobottszamok)+1, 1):
            if (item == i):
                dobottszamok[item]= dobottszamok[item]+1

    return dobottszamok



def szotarkiiratas(szotar:Dict[int, int]):
    for key, item in szotar.items():
        print(f"{key}: {item}")

def legtobbetdobottszam(szotar:Dict[int, int])->List[int]:
    legtobbetdobott:List[int]=[1]
    for i in range(2, 7, 1):
        if(szotar[i] == szotar[legtobbetdobott[0]]):
            legtobbetdobott.append(i)
        elif(szotar[i] > szotar[legtobbetdobott[0]]):
            legtobbetdobott.clear()
            legtobbetdobott.append(i)
 
    return legtobbetdobott

halmaz=listatoltes(elemszam)
print(f"a halmaz elemei: {halmaz}")
osszeg=listaosszeg(halmaz)
atlag=osszeg / elemszam
hatosokszama=hatosok(halmaz)
paratlaokszama=paratlanok(halmaz)
print(f"\nA halmaz átlaga: {atlag}\n{hatosokszama} db hatos lett dobva\n{paratlaokszama} db páratlan szám lett dobva.")

#bonusz
print("\n")
dobottszamok:Dict[int, int]=dobottszamokszama(halmaz)
szotarkiiratas(dobottszamok)
legtobbetdobottszamok:List[int]=legtobbetdobottszam(dobottszamok)
print(f"A legtöbbet dobott szám(ok) a {legtobbetdobottszamok}-es.")