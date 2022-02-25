import random
import time
import os
from typing import *

halmaz:List[int]=[]
halmazelemeinekszama:int=None
osszeg:int=None
atlag:float=None
ketjegyuszamokszama:int=None
paratlanszamokosszege:int=None
nullaravegzodoszamokszama:int=None
legmagasabbertek:int=None
legkisebbindexe:int=None

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

def listafeltoltese(elemekszama:int)->List[int]:
    lista:List[int]=[]
    for i in range(0, elemekszama, 1):
        lista.append(random.randint(-25, 25))
        #time.sleep(0.005)
    return lista

def halmazkiirasa(kiirasndohalmaz:List[int]):
    for item in kiirasndohalmaz:
        print(f"{item}", end="    ")

def halmazkiirasabutforditva(kiirasndohalmaz:List[int]):
    max:int=len(kiirasndohalmaz)-1
    for index in range(max, -1, -1):
        print(f"{kiirasndohalmaz[index]}", end="  ")

def sum(list:List[int])->int:
    eredmeny:int=0
    for item in list:
        eredmeny+=item

    return eredmeny

def halmazparoselemeinekkiirasa(kiirasndohalmaz:List[int]):
    for item in kiirasndohalmaz:
        if (item % 2 == 0):
            print(f"{item}", end="    ")

def halmazketjegyuszamaiszama(kiirasndohalmaz:List[int])->int:
    darabszam:int=0
    for item in kiirasndohalmaz:
        if abs(item)>9 and abs(item)<100:
            darabszam+=1

    return darabszam
            
def halmazegyjegyuelemeinekkiirasa(kiirasndohalmaz:List[int]):
    for item in kiirasndohalmaz:
        if abs(item)<10:
            print(f"{item}", end="    ")
        
def halmazparatlanszamainakszama(list:List[int])->int:
    eredmeny:int=0
    for item in list:
        if item % 2 == 1:
            eredmeny+=item

    return eredmeny

def halmaznullaravegzodoelemeinekszama(kiirasndohalmaz:List[int])->int:
    eredmeny:int=0
    for item in kiirasndohalmaz:
        if item % 10 == 0:
            eredmeny+=1

    return eredmeny

def halmaznovekvosorrend(kiirasndohalmaz:List[int])->List[int]:
    temp:int=None
    for i in range(0, len(kiirasndohalmaz)-1, 1):
        for j in range(i+1, len(kiirasndohalmaz), 1):
            if (kiirasndohalmaz[j]<kiirasndohalmaz[i]):
                temp=kiirasndohalmaz[i]
                kiirasndohalmaz[i]=kiirasndohalmaz[j]
                kiirasndohalmaz[j]=temp

    return kiirasndohalmaz

def halmazlegmagasabberteke(kiirasndohalmaz:List[int])->int:
    temp:int=kiirasndohalmaz[0]
    for i in range(1, len(kiirasndohalmaz), 1):
        if (temp<kiirasndohalmaz[i]):
            temp=kiirasndohalmaz[i]

    return temp

def halmazlegkisebbertekindexe(kiirasndohalmaz:List[int])->int:
    temp:int=0
    minimum:int=kiirasndohalmaz[temp]
    for i in range(1, len(kiirasndohalmaz), 1):
        minimum=kiirasndohalmaz[temp]
        if (minimum>kiirasndohalmaz[i]):
            minimum=kiirasndohalmaz[i]
            temp=i

    return temp

halmazelemeinekszama=elemszambekerese()
halmaz=listafeltoltese(halmazelemeinekszama)
os.system("cls")
print(" A halmaz elemei: ")
halmazkiirasa(halmaz)
rendezetthalmaz:List[int]=halmaz.copy()

print("\n A halmaz elemei fordított sorrendben:  ")
halmazkiirasabutforditva(halmaz)

print("\n A halmaz páros elemei:")
halmazparoselemeinekkiirasa(halmaz)

print("\n A halmaz egyjegyű számai:")
halmazegyjegyuelemeinekkiirasa(halmaz)

rendezetthalmaz=halmaznovekvosorrend(rendezetthalmaz)
print(f"\nA halmaz elemei növekvő sorrendben: {rendezetthalmaz}")

ketjegyuszamokszama=halmazketjegyuszamaiszama(halmaz)
print(f"\nKétjegyű számok száma a halmazban: {ketjegyuszamokszama}")

osszeg=sum(halmaz)
print(f"A halmaz elemeinek összege: {osszeg}")

paratlanszamokosszege=halmazparatlanszamainakszama(halmaz)
print(f"A halmaz páratlan számainak összege: {paratlanszamokosszege}")

atlag=osszeg/halmazelemeinekszama
print(f"A halmaz átlaga: {atlag}")

nullaravegzodoszamokszama=halmaznullaravegzodoelemeinekszama(halmaz)
print(f"A halmazban {nullaravegzodoszamokszama} db szám végződik 0-ra.")

legmagasabbertek=halmazlegmagasabberteke(halmaz)
print(f"A halmaz legnagyobb értéke: {legmagasabbertek}")

legkisebbindexe=halmazlegkisebbertekindexe(halmaz)
print(f"A halmazban a legkisebb érték indexe: {legkisebbindexe}")