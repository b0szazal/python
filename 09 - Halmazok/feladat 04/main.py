from typing import *
import random

halmaz:List[int]=[]
nemnegativhalmaz:List[int]=[]
csaknegativhalmaz:List[int]=[]
elemszam:int=random.randint(2, 10)


def halmazkitoltes(elemszama:int)->List[int]:
    lista:List[int]=[]
    generaltszam:int=None
    for i in range(0, elemszama, 1):
        generaltszam=random.randint(-100, 100)
        lista.append(generaltszam)

    return lista

def negativkivetel(halmaz:List[int])->List[int]:
    negativok:List[int]=[]
    nemnegativok:List[int]=[]
    for item in halmaz:
        if (item<0):
            negativok.append(item)
        else:
            nemnegativok.append(item)

    return nemnegativok, negativok

halmaz=halmazkitoltes(elemszam)
print(f"A halmaz összes eleme ({elemszam}db) :{halmaz}")
nemnegativhalmaz, csaknegativhalmaz=negativkivetel(halmaz)
print(f"\nA halmaz negatív elemei: {csaknegativhalmaz}\nnem negatív elemei: {nemnegativhalmaz}")