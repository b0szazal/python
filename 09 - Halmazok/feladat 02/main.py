import random
import time
import os
from typing import *

halmaz:List[int]=[]
elemszam:int=random.randint(2, 1000000)
osszeg:int=None
atlag:float=None
otszazfelettielemek:int=0

def listafeltoltes(elemekszama:int)->List[int]:
    randomszam:int=0
    lista:List[int]=[]
    pozitivvagynegativ:int=None
    for i in range(0, elemekszama, 1):
        pozitivvagynegativ=random.randint(0, 1)
        if pozitivvagynegativ == 1:
            randomszam=random.randint(100, 999)
        else:
            randomszam=random.randint(-999, -100)
        
        lista.append(randomszam)

    return lista

def halmazosszege(lista:List[int])->int:
    eredmeny:int=0
    for item in lista:
        eredmeny+=item

    return eredmeny

def halmazotszazfelettielemei(lista:List[int])->int:
    eredmeny:int=0
    for item in lista:
        if item > 500:
            eredmeny+=1

    return eredmeny

halmaz=listafeltoltes(elemszam)
print(f"A halmaz elemei: {halmaz}")
osszeg=halmazosszege(halmaz)
atlag=osszeg / elemszam
otszazfelettielemek=halmazotszazfelettielemei(halmaz)
print(f"\nA {elemszam} db elemű halmaz összege: {osszeg} \nátlaga: {atlag} \nés {otszazfelettielemek} db elem van 500 felett")